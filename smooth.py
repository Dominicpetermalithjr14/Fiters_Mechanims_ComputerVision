import cv2
import numpy as  np
from matplotlib import pyplot as plt
img = cv2.imread('cameraman.png')
#img_kernel = np.array([[0.111,0.111,0.111,0.111,0.111],[0.111,0.111,0.111,0.111,0.111],[0.111,0.111,0.111,0.111,0.111]])
#output_img = cv2.filter2D(src=img,ddepth= -1,kernel =img_kernel)
Gaussian_blur = cv2.GaussianBlur(src=img,ksize=(5,5),sigmaX=0,sigmaY=0)
#cv2.imshow("Original",img)
#cv2.imshow("Average filter",output_img)
plt.imshow(img)
plt.show()
plt.imshow(Gaussian_blur)
plt.show()
#cv2.waitKey(0)