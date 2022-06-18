import numpy as np
import matplotlib.pyplot as plt
import cv2 
from skimage.io import imread
from skimage.filters import roberts

img = cv2.imread("chile.jpg", cv2.IMREAD_GRAYSCALE)
op_roberts = roberts(img)

plt.imshow(op_roberts, cmap=plt.cm.gray)
plt.savefig('filtroRoberts.jpg', format='jpg')
