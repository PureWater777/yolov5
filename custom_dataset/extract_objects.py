import os
import glob
from PIL import Image
import cv2

from crop_images import crop_img
from get_parameters import get_parameters


images_path = "new_images/"
labels_path = "new_labels/"

cropped_imgs = []
images_files = glob.glob(os.path.join(images_path, "*jpg"))
text_files = glob.glob(os.path.join(labels_path, "*txt"))

os.mkdir("test0/")
os.mkdir("test1/")
os.mkdir("test2/")
os.mkdir("test3/")
os.mkdir("test4/")

num = 0
for idx, file in enumerate(text_files):
    params_list = get_parameters(file)
    img_path = images_files[idx]

    for object in params_list:
        cropped_img = crop_img(object, img_path)
        identifier = object[0]
        if identifier == "0":
            cropped_img.save(f"0/{num}.jpg")
        elif identifier == "1":
            cropped_img.save(f"1/{num}.jpg")
        elif identifier == "2":
            cropped_img.save(f"2/{num}.jpg")
        elif identifier == "3":
            cropped_img.save(f"3/{num}.jpg")
        elif identifier == "4":
            cropped_img.save(f"4/{num}.jpg")
        num += 1
        pass
