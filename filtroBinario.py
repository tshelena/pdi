import cv2 
img = cv2.imread('chile.jpg', 2) 
  
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
  
cv2.imwrite('filtroBinario.jpg', bw_img) 