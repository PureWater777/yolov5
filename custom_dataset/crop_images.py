import os
from math import floor

import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageOps


def crop_img(object, img_path):
    img = cv2.imread(img_path)
    pil_im = Image.open(img_path)
    pil_im_rotated = ImageOps.exif_transpose(pil_im)
    idx = object[0]
    center_x = float(object[1])
    center_y = float(object[2])
    width = float(object[3])
    height = float(object[4])

    img_h = img.shape[0]
    img_w = img.shape[1]

    left = int((center_x - width / 2) * img_w)
    right = int((center_x + width / 2) * img_w)
    top = int((center_y - height / 2) * img_h)
    bottom = int((center_y + height / 2) * img_h)

    if left < 0:
        left = 0
    if right > img_w - 1:
        right = img_w - 1
    if top < 0:
        t = 0
    if bottom > img_h - 1:
        bottom = img_h - 1

    crop_img = pil_im_rotated.crop((left, top, right, bottom))

    return crop_img