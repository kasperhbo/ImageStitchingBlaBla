import cv2
import numpy as np

from cut_off import Cutter
from straightener import Straightener
from stitcher import Stitcher

straighter = Straightener()
cutter = Cutter()
stitcher = Stitcher()

img_left = cv2.imread('assets/og/frame_left.png')
img_right = cv2.imread('assets/og/frame_right.png')

img_left = straighter.get_straightened_image(img_left)
img_right = straighter.get_straightened_image(img_right)

img_left   = cutter.get_left_cuttoff(img_left)
img_right = cutter.get_right_cuttoff(img_right)

combined = stitcher.stitch_images(img_left, img_right, 0,25,0)

while(1):
    #
    cv2.imshow('image_left', img_left)
    cv2.imshow('image_right', img_right)
    cv2.imshow('conbibed', combined)
    cv2.waitKey(0)



