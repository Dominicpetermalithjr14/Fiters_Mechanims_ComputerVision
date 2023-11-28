import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('cameraman.png')
mean = 0
stdev = 180
noise = np.zeros(img.shape, np.uint8)
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
out_img = cv2.filter2D(src=img,ddepth=-1,kernel=kernel)
#ci = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.randn(noise, mean, stdev)
cv2.imshow("median filter",out_img)
noisy_img = cv2.add(img, noise)
cv2.imshow("input", img)
#.imshow("noisy", noisy_img)
median_blur = cv2.medianBlur(src=img,ksize=9)
cv2.imshow("median",median_blur)

#cv2.imshow("noise", noise)
cv2.waitKey(0)
