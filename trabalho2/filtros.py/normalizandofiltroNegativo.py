import cv2
import numpy as np

img = cv2.imread("filtroNegativo.jpg")
img_new = cv2.normalize(img, None, alpha=0,beta=200, norm_type=cv2.NORM_MINMAX)

img_new = img_new.astype(np.uint8) 
cv2.imwrite('normalizandofiltroNegativo.jpg', img_new) 

