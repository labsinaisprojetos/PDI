import cv2
import numpy as np
import matplotlib.pyplot as plt

#Loading the image
img = cv2.imread('moon.jpg', 1)

#Calculating its histogram
counts, binLocation = np.histogram(img)
maxCount = np.amax(counts[:])

# Loop over clip ratios
clipRatio = [1, 0.7, 0.4, 0.1] #Ratio 1 means no clipping
limitEqImg = []
LUT = np.zeros((len(clipRatio), 256))

for i in range(1, len(clipRatio)):
    # Clip histogram
    clip = clipRatio[i]*maxCount
    clippedCounts = (counts < clip)*counts + (counts >=clip)*clip

    # Construct a 1 dimensional virtual image for histeq to get mapping function
    clippedImg = []
    for level in range(0, 255):
        clippedImg = np.hstack((clippedImg, level*np.ones(1, clippedCounts(level + 1))))
