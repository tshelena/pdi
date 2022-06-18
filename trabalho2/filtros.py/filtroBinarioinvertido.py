import cv2 
img = cv2.imread('chile.jpg', cv2.IMREAD_GRAYSCALE)
  
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) 
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) 
  
cv2.imwrite('filtroBinarioinvertido.jpg', bw_img) 