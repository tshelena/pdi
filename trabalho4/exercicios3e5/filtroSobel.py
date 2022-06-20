import numpy as np
import cv2

matriz = np.array([[15, 18, 13, 16, 20], [30, 37, 40, 32, 28], [16, 10, 15, 18, 14], [70, 77, 66, 55, 60]])

matriz = matriz.astype(np.uint8)

sobelX = cv2.Sobel(matriz, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(matriz, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobel = cv2.bitwise_or(sobelX, sobelY)

print (np.matrix(sobel))