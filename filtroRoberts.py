import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import roberts

img = cv2.imread('chile.jpg', 0)
op_roberts = roberts(img)

img_new = img_new.astype(op_roberts) 
cv2.imwrite('filtroRoberts.jpg', img_new)


