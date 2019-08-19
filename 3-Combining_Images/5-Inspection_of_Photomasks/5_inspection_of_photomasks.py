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
 Image subtraction example from IC manufacturing:
 die-to-die comparison of photomasks
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
import cv2

#Load text images
maskImg1 = cv2.imread("mask1.png",0)
maskImg2 = cv2.imread("mask2.png",0)

diffImg = abs(maskImg1 - maskImg2)
plt.gray()
plt.imshow(diffImg);
plt.axis('Off')
plt.title('Difference Image')
cv2.imwrite('Mask_Comparison_diff.png',diffImg)


