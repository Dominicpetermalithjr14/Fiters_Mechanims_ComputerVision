import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('cameraman.png')
mean = 0
stdev = 180
noise = np.zeros(img.shape,np.uint8)
ci = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.randn(noise,mean,stdev)
noisy_img = cv2.add(img,noise)
cv2.imshow("input",img)
cv2.imshow("noisy",noisy_img)
cv2.imshow("noise",noise)
cv2.waitKey(0)