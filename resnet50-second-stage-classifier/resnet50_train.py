import math, json, os, sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
os.environ['SM_FRAMEWORK'] = 'tf.keras'
import tensorflow
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import image


DATA_DIR = '../resenet_final/data/'
TRAIN_DIR = os.path.join(DATA_DIR, 'train')
VALID_DIR = os.path.join(DATA_DIR, 'valid')
SIZE = (224, 224)
BATCH_SIZE = 16

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
print(len(tensorflow.config.list_physical_devices('GPU')))

if __name__ == "__main__":
    with tensorflow.device('/device:gpu:0'):
        num_train_samples = sum([len(files) for r, d, files in os.walk(TRAIN_DIR)])
        num_valid_samples = sum([len(files) for r, d, files in os.walk(VALID_DIR)])

        num_train_steps = math.floor(num_train_samples/BATCH_SIZE)
        num_valid_steps = math.floor(num_valid_samples/BATCH_SIZE)

        gen = tensorflow.keras.preprocessing.image.ImageDataGenerator()
        val_gen = tensorflow.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True, vertical_flip=True)


        batches = gen.flow_from_directory(TRAIN_DIR, target_size=SIZE, class_mode='categorical', shuffle=True, batch_size=BATCH_SIZE)
        val_batches = val_gen.flow_from_directory(VALID_DIR, target_size=SIZE, class_mode='categorical', shuffle=True, batch_size=BATCH_SIZE)

        model = tensorflow.keras.applications.resnet50.ResNet50()

        classes = list(iter(batches.class_indices))
        model.layers.pop()
        for layer in model.layers:
            layer.trainable=False
        last = model.layers[-1].output
        x = Dense(len(classes), activation="softmax")(last)
        finetuned_model = Model(model.input, x)
        finetuned_model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
        for c in batches.class_indices:

            classes[batches.class_indices[c]] = c
        finetuned_model.classes = classes

        early_stopping = EarlyStopping(patience=10)
        checkpointer = ModelCheckpoint('resnet50_best.h5', verbose=1, save_best_only=True)

        finetuned_model.fit(batches, steps_per_epoch=num_train_steps, epochs=1000, callbacks=[early_stopping, checkpointer], validation_data=val_batches, validation_steps=num_valid_steps)
        finetuned_model.save('resnet50_final.h5')
