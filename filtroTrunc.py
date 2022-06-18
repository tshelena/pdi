import numpy as np
import cv2

img = cv2.imread("chile.jpg", cv2.IMREAD_GRAYSCALE)
thresh = 127
maxValue = 255
th, dst = cv2.threshold(img, thresh, maxValue, cv2.THRESH_TRUNC)

cv2.imwrite('filtroTrunc.jpg', dst)
