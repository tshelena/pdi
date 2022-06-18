import cv2 
import numpy as np
import matplotlib.pyplot as plt 
   
img = cv2.imread('chile.jpg', 1) 

m, n, _ = img.shape 

for i in range(0, m - 1): 
    for j in range(0, n - 1): 
        
        temp = img[i, j] 
        temp[0] = 255 - temp[0] 
        temp[1] = 255 - temp[1] 
        temp[2] = 255 - temp[2] 
        img[i, j] = temp 

img = img.astype(np.uint8) 
cv2.imwrite('filtroNegativo.jpg', img) 