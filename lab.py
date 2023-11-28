import cv2
import numpy as np
#read image
img=cv2.imread("cameraman.png",0)
cv2.imshow("camera man",img)
#size of the image
img2=img[20:100,100:250]
cv2.imshow("Extracted camerman", img2)
cv2.waitKey(0)