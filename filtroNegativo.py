import cv2 
import numpy as np
import matplotlib.pyplot as plt 
  
  
img = cv2.imread('chile.jpg', 1) 

m, n, _ = img.shape 
 
img_new = np.zeros([m,n]) 
for i in range(0, m - 1): 
    for j in range(0, n - 1): 
        
        pixel = img[i, j] 
        
      
        pixel[0] = 255 - pixel[0] 
        
        pixel[1] = 255 - pixel[1] 
        
        pixel[2] = 255 - pixel[2] 
        
        img_new[i, j] = pixel 

img_new = img_new.astype(np.uint8)
cv2.imwrite('filtroNegativo.jpg', img_new)
