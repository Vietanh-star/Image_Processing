import numpy as np
import cv2

img = np.uint8([[[25, 113, 147]]])
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 21 33 180
print(hsv_img)
img2 = cv2.imread('mecanum.jpg')                   
hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV) 

min = np.array([20, 20, 170])
max = np.array([25, 35, 190])
mask = cv2.inRange(hsv_img2, min, max)
final = cv2.bitwise_and(img2, img2, mask= mask)
cv2.imshow('sub Title', final)
cv2.waitKey(0)