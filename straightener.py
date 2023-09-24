import cv2
import numpy as np

k1 = 0.1720
k2 = -0.3570
k3 = 0.0510
# k1 = 0.1620, k2 = -0.5370, k3 = -0.0590
# k1 = 0.1620, k2 = -0.5370, k3 = -0.0190
k1 = 0.1620
k2 = -0.5370
k3 = -0.0590

# k1 = 0.0620, k2 = -0.5770, k3 = -0.0890


# k1 = 0.0920, k2 = -0.5370, k3 = -0.0590 values export 2  img_left

coefficients = [k1, k2, k3]  # Initial values for [k1, k2, k3]
dist_coeff = np.array([coefficients[0], coefficients[1], coefficients[2], 0, 0])

class Straightener:

    def get_straightened_image(self, image):

        camera_matrix = np.array([[3000, 0, image.shape[1] / 2], [0, 3000, image.shape[0] / 2], [0, 0, 1]], dtype="double")

        # dist_coeff = np.array([k1, k2, k3, 0, 0])
        return cv2.undistort(image, camera_matrix, dist_coeff)


straight = Straightener()

img = cv2.imread('assets/og/frame_right.png')
# img = straight.get_straightened_image(img)

active_coeff = 0  # Start with k1

while True:
    camera_matrix = np.array([[3000, 0, img.shape[1] / 2], [0, 3000, img.shape[0] / 2], [0, 0, 1]], dtype="double")

    dist_coeff = np.array([coefficients[0], coefficients[1], coefficients[2], 0, 0])
    undistorted_img = cv2.undistort(img, camera_matrix, dist_coeff)

    # Show the undistorted image
    cv2.imshow('Undistorted Image', undistorted_img)
    key = cv2.waitKey(0)
    print(key)

    # Adjust coefficients using arrow keys
    if key == 2:  # Left arrow
        active_coeff = (active_coeff - 1) % 3
        print(key)
    elif key == 3:  # Right arrow
        active_coeff = (active_coeff + 1) % 3
    elif key == 0:  # Up arrow
        coefficients[active_coeff] += 0.01
    elif key == 1:  # Down arrow
        coefficients[active_coeff] -= 0.01
    elif key == ord('q'):  # Quit on 'q'
        break


    print(f"k1 = {coefficients[0]:.4f}, k2 = {coefficients[1]:.4f}, k3 = {coefficients[2]:.4f}")
cv2.imwrite('assets/export/test2/img_right.png', undistorted_img)

