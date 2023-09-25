# # import cv2
# # import numpy as np
# #
# # from cut_off import Cutter
# # from straightener import Straightener
# # from stitcher import Stitcher
# #
# # straighter = Straightener()
# # cutter = Cutter()
# # stitcher = Stitcher()
# #
# # img_left = cv2.imread('assets/og/frame_left.png')
# # img_right = cv2.imread('assets/og/frame_right.png')
# #
# # img_left = straighter.get_straightened_image(img_left)
# # img_right = straighter.get_straightened_image(img_right)
# #
# # img_left   = cutter.get_left_cuttoff(img_left)
# # img_right = cutter.get_right_cuttoff(img_right)
# #
# # combined = stitcher.stitch_images(img_left, img_right, 0,25,0)
# #
# # while(1):
# #     #
# #     cv2.imshow('image_left', img_left)
# #     cv2.imshow('image_right', img_right)
# #     cv2.imshow('conbibed', combined)
# #     cv2.waitKey(0)
# #
# #
# #
# # import required libraries
# import cv2
# import numpy as np
#
# # read input image
# import cv2
#
# im = cv2.imread('assets/og/test_left.png', cv2.IMREAD_GRAYSCALE)
# flags = cv2.CALIB_CB_NORMALIZE_IMAGE | cv2.CALIB_CB_EXHAUSTIVE | cv2.CALIB_CB_ACCURACY
# retval, corners = cv2.findChessboardCornersSB(im, (8, 5), flags=flags)
# im_rgb = cv2.imread('assets/og/test_left.png', cv2.IMREAD_COLOR)
# drawn = cv2.drawChessboardCorners(im_rgb, (8, 5), corners, retval)
# cv2.imshow('test', drawn)
# cv2.waitKey(0)
#
# # cv2.imwrite('corners.png', drawn)
# # cv2.findChessboardCornersSB(image, cv::Size(18,12), corners, cv::CALIB_CB_EXHAUSTIVE | cv::CALIB_CB_ACCURACY);
# # GRID = (7, 7)
# # found, corners = cv2.findChessboardCorners(
# #     img_captured, GRID, cv2.CALIB_CB_ADAPTIVE_THRESH)
# #
# # cv2.drawChessboardCorners(img_captured_corners, GRID, corners, found)
# # cv2.imshow('img_captured_corners', img_captured_corners)
#
# # # convert the input image to a grayscale
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #
# # # Find the chess board corners
# # ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)
# #
# # # if chessboard corners are detected
# # if ret == True:
# #     # Draw and display the corners
# #     img = cv2.drawChessboardCorners(img, (7, 6), corners, ret)
# #     cv2.imshow('Chessboard', img)
# #     cv2.waitKey(0)
# # cv2.destroyAllWindows()
# !/usr/bin/env python
