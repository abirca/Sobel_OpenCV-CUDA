# -*- coding: utf-8 -*-
"""Sobel_with_OpenCV_CUDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rug5SaOlpcVdiEtXENJqOMWwWp4gNylM

# Filtro de Sobel

> ## *Comparacion del filtro de Sobel implementado en CPU, OpenCV y CUDA*
"""

print("Sistema operativo usado: ")
!lsb_release -a
print(">>>> Clone Repository...")
!git clone https://github.com/LevidRodriguez/Sobel_with_OpenCV-CUDA.git
# %cd Sobel_with_OpenCV-CUDA
print (">>> Setup CUDA...")
!pip install git+git://github.com/andreinechaev/nvcc4jupyter.git
# %load_ext nvcc_plugin
print(">>> Compiling...")
!make all
print(">>> Run program...")
# use: ./sobelFilter <srcimg>
# !./sobelFilter images/lena.jpg
# !./sobelFilter images/DJI_0748.JPG
# !./sobelFilter images/DJI_0832.JPG
# !./sobelFilter images/DJI_0659.JPG
# !./sobelFilter images/DJI_0189.JPG
# !./sobelFilter images/DJI_0257.JPG
!./sobelFilter images/DJI_0279.JPG
print ("nvprof: ")
!nvprof ./sobelFilter images/DJI_0279.JPG
print(">>> Downloading results...")
from google.colab import files
print("    >>> Downloading outImgCPU.png...")
files.download("outImgCPU.png")
print("    >>> Downloading outImgOpenCV.png...")
files.download("outImgOpenCV.png")
print("    >>> Downloading outImgGPU.png...")
files.download("outImgGPU.png")
print(">>> Remove repository...")
# %cd ..
!rm -r Sobel_with_OpenCV-CUDA/
print(">>> Done <<<<")

"""## Si el programa ha fallado...

> Elimar directorio para nuevas pruebas
"""

print(">>> Clean...")
print(">>> Remove repository...")
# %cd ..
!rm -r Sobel_with_OpenCV-CUDA/
print(">>> Done <<<<")

"""## Drive"""

# Ejecuta esta celda para activar Google Drive.
from google.colab import drive
drive.mount('/content/drive')