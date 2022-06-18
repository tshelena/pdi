import numpy as np
import cv2

img = cv2.imread('chile.jpg', 1)

kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
img_new = cv2.filter2D(img, -1, kernel)
cv2.imwrite('filtroSharpen.jpg', img_new) 