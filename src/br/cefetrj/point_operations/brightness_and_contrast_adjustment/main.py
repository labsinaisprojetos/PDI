import cv2
import numpy as np
import matplotlib.pyplot as plt

#loading the image
img = cv2.imread('parrot.jpg')
img = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

#Brightness adjustment by intensity scaling
scale = 1.2
scaledImg = scale*img

#Normalizying the scaled image
#scaledImg *= 255.0/scaledImg.max()
#limiar em 255

# Plot original image
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Original Image')
# Plot scaled image
plt.subplot(1, 3, 2)
plt.imshow(scaledImg)
plt.title('Scaled Image')
cv2.imwrite('Brightness_scaled.png', scaledImg)

#Contrast adjustment by changing "gamma"
gamma = 1.5
gammaImg = img**gamma

#Normalizying the gamma image
gammaImg *= 255.0/gammaImg.max()

# Plot gamma image
plt.subplot(1, 3, 3)
plt.imshow(gammaImg.astype(np.uint8))
plt.title('Gamma Image')
cv2.imwrite('Contrast_gamma.png', gammaImg)

plt.show()
