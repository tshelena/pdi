import numpy as np
import matplotlib.pyplot as plt
import cv2 
from skimage.io import imread
from skimage.filters import prewitt

img = cv2.imread("chile.jpg", cv2.IMREAD_GRAYSCALE)
op_prewitt = prewitt(img)

plt.imshow(op_prewitt, cmap=plt.cm.gray)
plt.savefig('filtroPrewitt.jpg', format='jpg')




