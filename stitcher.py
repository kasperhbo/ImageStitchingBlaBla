import numpy as np

class Stitcher:

    def shift_image_vertically(self, image, shift):
        """
        Shifts an image along the y-axis.

        Parameters:
        - image: The input image (2D or 3D array).
        - shift: The number of pixels to shift. Positive values shift downward, negative values shift upward.

        Returns:
        - Shifted image.
        """

        if len(image.shape) == 2:  # For grayscale images
            pad_width = ((abs(shift), 0), (0, 0))
        elif len(image.shape) == 3:  # For RGB images
            pad_width = ((abs(shift), 0), (0, 0), (0, 0))
        else:
            raise ValueError("Invalid image shape")

        if shift > 0:  # Shift downward
            return np.pad(image, pad_width=pad_width, mode='constant')[:-shift]
        elif shift < 0:  # Shift upward
            return np.pad(image, pad_width=pad_width, mode='constant')[-shift:]
        else:  # No shift
            return image

    def stitch_images(self, image_left, image_right, right_x_shift, right_y_shift, right_alpha):
        # shift = ;
        image_right = self.shift_image_vertically(image_right, right_y_shift)
        return np.concatenate((image_left, image_right), axis=1)

        ##old code
        h_left, w_left, _ = image_left.shape
        h_right, w_right, _ = image_right.shape

        # Adjust canvas size
        h_canvas = max(h_left, h_right + abs(right_y_shift))
        w_canvas = w_left + w_right

        canvas = np.zeros((h_canvas, w_canvas, 3), dtype=float)
        canvas[:h_left, :w_left] = image_left

        # Blend img_right based on its current shift
        y_end = min(right_y_shift + h_right, h_canvas)
        x_end = min(right_x_shift + w_left + w_right, w_canvas)

        for c in range(3):
            canvas[right_y_shift:y_end, right_x_shift + w_left:x_end, c] = (
                    (1 - right_alpha) * canvas[right_y_shift:y_end, right_x_shift + w_left:x_end,
                                        c] + right_alpha * image_right[:y_end - right_y_shift,
                                                           :x_end - right_x_shift - w_left, c])

        return (canvas * 255).astype(np.uint8)

