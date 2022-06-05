import os
import shutil

directory = "labels"
new_directory = "labels_combined"
list_of_folders = os.listdir(directory)
os.mkdir(new_directory)

#combining files
for folder_name in list_of_folders:
    for file_name in os.listdir(os.path.join(directory, folder_name)):
        shutil.copy(os.path.join(directory, folder_name, file_name), new_directory)

