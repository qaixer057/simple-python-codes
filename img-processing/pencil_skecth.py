import cv2

img = cv2.imread('target.png', 1)

import matplotlib.pyplot as plt
# plt.imshow(img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(img_gray)

img_invert = cv2.bitwise_not(img_gray)

# plt.imshow(img_invert)

img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)

plt.imshow(img_smoothing)

def sketch(x, y):
    return cv2.divide(x, 255 - y, scale=256)

final_img = sketch(img_gray, img_smoothing)

plt.imshow(final_img)

cv2.imwrite('Qaiser_DP.jpg',final_img)
