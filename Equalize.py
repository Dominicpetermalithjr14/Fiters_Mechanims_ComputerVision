import cv2
import matplotlib.pyplot as plt

# load the image

image_path = 'cameraman.png' 
image = cv2.imread(image_path, 0)

# perform histogram equalization
equalized_image = cv2.equalizeHist(image)

# display the original and equalize image

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')
