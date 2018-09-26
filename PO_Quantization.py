import cv2 as cv
import math as mt
import numpy as np
import matplotlib.pyplot as plt
# import skimage.measure as sm
# import skimage.transform as st
CONST_BITS = 8
img=cv.imread('face.img')
for numBits in CONST_BITS:
    numLevel = 2.^numBits
    levelGap = 256 / numLevel
    aux = img/levelGap
    quantizedImg= np.dtype.uint8((mt.ceil(aux))* levelGap -1)

# # """EXIBINDO IMAGENS NA TELA"""
    # fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 4), sharex=True, sharey=True)
    # ax1.axis('off')
    # ax1.imshow(cv_thresh,cmap=plt.cm.gray)
    # ax1.set_title('Original')
    # ax2.axis('off')
    # ax2.imshow(cv_thresh_Mo,cmap=plt.cm.gray)
    # ax2.set_title('OpenCv Closed')
    # ax3.axis('off')
    # ax3.imshow(cv_thresh_La,cmap=plt.cm.gray)
    # ax3.set_title('OpenCv Closed & Labeled')
    # plt.show()
