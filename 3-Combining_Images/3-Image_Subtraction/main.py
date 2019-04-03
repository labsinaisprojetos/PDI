import cv2
import numpy as np
import matplotlib.pyplot as plt

#Loading the images
mskImg = cv2.imread('mask.jpg', 1)
mskImg = cv2.normalize(mskImg.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
liveImg = cv2.imread('live.jpg', 1)
liveImg = cv2.normalize(liveImg.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

print(mskImg.shape)

#Calculate difference image and enhance contrast
diffImg = abs(np.subtract(mskImg, liveImg))
#histeqDiffImg = adapthisteq(diffImg, 'ClipLimit', 0.005)

#Show the results
plt.subplot(1, 3, 1)
plt.imshow(liveImg)
plt.title('Live Image')

plt.subplot(1, 3, 2)
plt.imshow(mskImg)
plt.title('Mask Image')

plt.subplot(1, 3, 3)
plt.imshow(diffImg)
plt.title('Difference Image')

plt.show()


