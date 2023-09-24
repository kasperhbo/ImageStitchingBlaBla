import cv2
import numpy as np


# Read the image
# image_left = cv2.imread('assets/export/left_straightened_image.png')
# image_right = cv2.imread('assets/export/right_straightened_image.png')
#

class Cutter:
    def get_right_cuttoff(self, right_image, amount_in_pixels = 3680):
        cut_off = right_image.shape[1] - amount_in_pixels
        return self.cut_off_image(right_image, cut_off, 0)

    def get_left_cuttoff(self, left_image, amount_in_pixels = 221):
        cut_off = amount_in_pixels
        return self.cut_off_image(left_image, 0, cut_off)

    def cut_off_image(self, image, left, right):
        if left >0:
            image = image[:, left:]
        if right >0:
            image = image[:, :-right]

        return image


#
# cv2.imshow('left', image_left)
# cv2.imshow('right', image_right)
# # cv2.imshow('right', image_right)
#
# cv2.waitKey(0)