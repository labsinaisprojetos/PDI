"""    CEFET-RJ - UNED Nova Iguaçu
   Dep. Engenharia de Controle e Automação 
 Disciplina: Processamento Digital de Imagens
 - Professor: Gabriel Matos Araujo
 - Material de Aula (Conversão em Python)
 - Script escrito por Pedro Monforte

           Original File Heading
 EE368/CS232 Digital Image Processing
 Bernd Girod
 Department of Electrical Engineering, Stanford University 

 Script by Qiyuan Tian and David Chen
 Histogram equalization example
"""
#%%
import cv2
import matplotlib.pyplot as plt

# Load test image
img = cv2.imread('bay.jpg',0)
#img = cv2.imread('brain.jpg',0)
#img = cv2.imread('moon.jpg',0)

# Perform histogram equalization
eqImg = cv2.equalizeHist(img)

# Comparing Images
plt.gray() # set the color map to grayscale in matplotlib
figs, axs = plt.subplots(1, 2, figsize=(10, 3))
titlelist = ['original image','equalized image']
imagelist = [img,eqImg]
for ax,title,fig in zip(axs,titlelist,imagelist):
    ax.imshow(fig,vmax=255,vmin=0)
    ax.set_title(title.capitalize())
    ax.axis('off')

# Plotting histograms
figs, axs = plt.subplots(1, 2, figsize=(10, 3))
for ax,title,fig in zip(axs,titlelist,imagelist):
    ax.hist(fig.flatten(),256,[0,256], color = 'r')
    ax.set_title(title.capitalize())
    ax.axis('on')



