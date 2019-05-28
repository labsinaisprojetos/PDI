import cv2
import numpy as np
import matplotlib.pyplot as plt

#loading the image
img = cv2.imread('face.jpg', 1)

#Loop over the number of the bits
for numOfBit in range(1, 9):
    # Quantize to given number of bits
    numOfLevel = 2.0**numOfBit
    levelGap = 256 / numOfLevel
    #quantizedImg = np.subtract(np.multiply(np.ceil(np.true_divide(img, levelGap)), levelGap), 1)
    quantizedImg = np.ceil(img / levelGap) * levelGap - 1

    # Plot image
    plt.subplot(2, 4, 9 - numOfBit)
    plt.imshow(quantizedImg.astype(np.uint8))
    plt.title(numOfBit)

plt.show()
