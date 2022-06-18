import numpy as np
import matplotlib.pyplot as plt
import cv2 
from skimage.io import imread
from skimage.filters import sobel

img = cv2.imread("chile.jpg", cv2.IMREAD_GRAYSCALE)
op_sobel = sobel(img)

plt.imshow(op_sobel, cmap=plt.cm.gray)
plt.savefig('filtroSobel.jpg', format='jpg')
