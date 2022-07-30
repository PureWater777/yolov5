This is a custom implementation of yolov5 algorithm. It aims to compare the workings of the algoirthm in its default form as well as with the custom second-stage classifier.
The labels for the yolo were created in makesense.ai. Aditionally a number of scripts were prepared to switch the format of the labels, divide available images into train, test, and val samples, rotate the images to their initial position, and finally extract single objects from the initial images to create a separate dataset for the purpose of training resnet50 classifier.
To run the application:
1. Set the Anaconda environment with GPU training support according to: https://developpaper.com/windows-pychar-yolov5-configuration-environment-and-local-training-model/.
2. Create a 'images' directory in 'custom_dataset' and paste the contents of https://drive.google.com/drive/folders/18OyUSMt2qpTo0SN3FspR25Q7cAWPxweL?usp=sharing.
3. Select the default model and run the algorithm according to: https://docs.ultralytics.com/tutorials/train-custom-datasets/.
As to prepare the data for the second-stage classifier:
1. Update the paths in 'custom_dataset/divide_labels.py' and 'custom_dataset/extract_objects.py'.
3. Move the newly created dataset with the classes divided by the class labels to 'resnet50-second-stage-classifier/data'.
4. Train the the model by running 'resnet50_train.py'.
5. Apply the classifier in 'general.py'.

The algorithm was also tested on freiburg groceries dataset which is available under: http://aisdatasets.informatik.uni-freiburg.de/freiburg_groceries_dataset/.

As the annotations are saved in xml, a script was created to convert them to yolo format ('groceries_dataset/xml2yolo.py').
With the use of 'divide_labels.py' label data is split into train, test, and val subsets.

It is advisable to also install wandb as it allows to aggregate the results and switch around many different tresholds for testing pursposes.
