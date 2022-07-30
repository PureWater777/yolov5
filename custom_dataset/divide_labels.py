import random
import glob
import os
import shutil
import math


path = "D:/Projects/Python/MGR/yolov5/custom_dataset/"
label_dir = "labels/"
image_dir = "images/"
lower_limit = 0
subsets = {"train": 0.8, "val": 0.1, "test": 0.1}

files = glob.glob(os.path.join(label_dir, '*.txt'))
random.shuffle(files)
train_limit = math.floor((len(files)) * subsets["train"])
test_limit = math.floor((len(files)) * (subsets["train"] + subsets["test"]))
files_paths = [(path + file).replace("\\", "/").replace(".txt", ".png").replace("labels", "images").replace("images", "images") for file in files]

files_train = files_paths[lower_limit:train_limit]
files_test = files_paths[train_limit:test_limit]
files_val = files_paths[test_limit:]


with open("train.txt", "a", encoding='utf8') as f:
    f.writelines("\n".join(files_train))
    f.write("\n")
with open("test.txt", "a", encoding='utf8') as f:
    f.writelines("\n".join(files_test))
    f.write("\n")
with open("val.txt", "a", encoding='utf8') as f:
    f.writelines("\n".join(files_val))
    f.write("\n")

with open("train.txt", "r") as f:
    for line in f:
        tab = line.split("/")
        fixed_tab = tab[:7] + tab[8:]
        fixed_path = "/".join(fixed_tab)
        with open ("train_fixed.txt", "a") as new_file:
            new_file.write(fixed_path)

with open("test.txt", "r") as f:
    for line in f:
        tab = line.split("/")
        fixed_tab = tab[:7] + tab[8:]
        fixed_path = "/".join(fixed_tab)
        with open ("test_fixed.txt", "a") as new_file:
            new_file.write(fixed_path)

with open("val.txt", "r") as f:
    for line in f:
        tab = line.split("/")
        fixed_tab = tab[:7] + tab[8:]
        fixed_path = "/".join(fixed_tab)
        with open ("val_fixed.txt", "a") as new_file:
            new_file.write(fixed_path)