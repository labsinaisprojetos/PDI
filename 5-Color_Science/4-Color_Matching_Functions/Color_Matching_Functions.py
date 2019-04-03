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
 Spectral matching functions

 colorMatchingFunction.mat: Stiles & Burch (1959) 10-deg, RGB CMFs
 Reference: http://cvrl.ioo.ucl.ac.uk/cmfs.htm
"""
#%%
import numpy as np
from numpy import genfromtxt as load
import matplotlib.pyplot as plt

# Load color matching functions
CMFs = load('CMF.csv', delimiter=',')
wavelength = np.copy(CMFs[:,0])
xyz = (CMFs[:, 1:4]).copy()

for i,cmf in zip(range(3),["r","g","b"]):
   plt.plot(wavelength,xyz[:,i],cmf,label=(cmf+r"($\lambda$)"),linewidth=2)

plt.xlabel(r'Wavelength $\lambda$ (nm)',fontsize=13)
plt.ylabel('Tristimulus values',fontsize=13)
plt.title('CIE color matching functions',fontsize=15)

plt.axis([390,760,-0.5,3.5])
plt.legend()
plt.grid(True)
plt.savefig('Color_Matching_Functions_rgbmatching.png')