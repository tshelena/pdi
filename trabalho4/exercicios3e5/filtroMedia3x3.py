import cv2 
import numpy as np 
    
matriz = np.array([[15, 18, 13, 16, 20], [30, 37, 40, 32, 28], [16, 10, 15, 18, 14], [70, 77, 66, 55, 60]])

print (np.matrix(matriz))

m, n = matriz.shape 

mask = np.ones([3, 3], dtype = int) 
mask = mask / 9
   
Y = np.zeros([m, n]) 
  
for i in range(1, m-1): 
    for j in range(1, n-1): 
        temp = matriz[i-1, j-1]*mask[0, 0]+matriz[i-1, j]*mask[0, 1]+matriz[i-1, j + 1]*mask[0, 2]+matriz[i, j-1]*mask[1, 0]+ matriz[i, j]*mask[1, 1]+matriz[i, j + 1]*mask[1, 2]+matriz[i + 1, j-1]*mask[2, 0]+matriz[i + 1, j]*mask[2, 1]+matriz[i + 1, j + 1]*mask[2, 2] 
        Y[i, j]= temp 

print (np.matrix(Y))