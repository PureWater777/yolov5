This is a custom implementation of yolov5 algorithm. It aims to compare the workings of the algoirthm in its default form as well as with the custom second-stage classifier.
The labels for the yolo were created in makesense.ai. Aditionally a number of scripts were prepared to switch the format of the labels, divide available images into train, test, and val samples, rotate the images to their initial position, and finally extract single objects from the initial images to create a separate dataset for the purpose of training resnet50 classifier.
To run the application:
1. Create a 'images' directory in 'custom_dataset' and paste the contents of https://drive.google.com/drive/folders/18OyUSMt2qpTo0SN3FspR25Q7cAWPxweL?usp=sharing.

2. Update the paths in 'custom_dataset/divide_labels.py' and 'custom_dataset/extract_objects.py'.
3. Move the newly created dataset with the classes divided by the class_label to 'resnet50-second-stage-classifier'.
4. Train the
