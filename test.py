from scipy.misc import imread,imsave
import numpy as np
import cv2
import time
from converter import *

newimg=RBG_to_dilation(img)
imsave('./images/dog_to_line.png',newimg)

newimg=cv2.imread('dog.png', cv2.IMREAD_GRAYSCALE)
imsave('./images/dog_to_grey.png',newimg)

newimg=RBG_to_YUV(img)
newimg[:,:,0]=0
imsave('./images/dog_RBG_to_UV.png',newimg)

newimg=YUV_to_RGB(newimg)
imsave('./images/dog_UV_to_RGB.png',newimg)

grey=imread('./images/dog_to_grey.png').astype('float32')
grey_to_RGB = cv2.cvtColor(grey, cv2.COLOR_GRAY2RGB )

UV=RBG_to_YUV(img)
UV[:,:,0]=0
color_to_RGB=YUV_to_RGB(UV)
back=grey_to_RGB+color_to_RGB
img=imread('dog.png')[:,:,:3].astype('float32')
print(np.max(back-img),np.min(back-img))
imsave('./images/dog_back_to_color.png',grey_to_RGB+color_to_RGB)



img=imread('anime.jpg')[:,:,:3].astype('float32')
newimg=RBG_to_dilation(img)
imsave('./images/anime_to_line.png',newimg)

newimg=cv2.imread('anime.jpg', cv2.IMREAD_GRAYSCALE)
imsave('./images/anime_to_grey.png',newimg)

newimg=RBG_to_YUV(img)
newimg[:,:,0]=0
imsave('./images/anime_to_UV.png',newimg)

newimg=YUV_to_RGB(newimg)
imsave('./images/anime_UV_to_RGB.png',newimg)

grey=imread('./images/anime_to_grey.png').astype('float32')
grey_to_RGB = cv2.cvtColor(grey, cv2.COLOR_GRAY2RGB )

UV=RBG_to_YUV(img)
UV[:,:,0]=0
color_to_RGB=YUV_to_RGB(UV)

back=grey_to_RGB+color_to_RGB
img=imread('anime.jpg')[:,:,:3].astype('float32')

imsave('./images/anime_back_to_color.png',grey_to_RGB+color_to_RGB)
