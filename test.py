from scipy.misc import imread,imsave
import cv2
import os
from utils import RBG_to_dilation,RBG_to_YUV,YUV_to_RGB

if not os.path.exists('Convert_images'):
    os.mkdir('Convert_images')

ORI_PATH = os.path.join('Original_Images')
CON_PATH = os.path.join('Convert_Images')
full_file_names = os.listdir(ORI_PATH)
for full_file_name in full_file_names:
    FULL_PATH = os.path.join(ORI_PATH,full_file_name)
    file_name = os.path.basename(FULL_PATH).split('.')[0]
    img=cv2.imread(FULL_PATH)
    imsave(os.path.join(CON_PATH,full_file_name),img)

    newimg=RBG_to_dilation(img)
    imsave(os.path.join(CON_PATH,file_name+'_to_line.png'),newimg)

    newimg=cv2.imread(FULL_PATH, cv2.IMREAD_GRAYSCALE)
    imsave(os.path.join(CON_PATH,file_name+'_to_grey.png'),newimg)

    newimg=RBG_to_YUV(img)
    newimg[:,:,0]=0
    imsave(os.path.join(CON_PATH,file_name+'_RBG_to_UV.png'),newimg)

    newimg=YUV_to_RGB(newimg)
    imsave(os.path.join(CON_PATH,file_name+'_UV_to_RGB.png'),newimg)

    grey=imread(os.path.join(CON_PATH,file_name+'_to_grey.png')).astype('float32')
    grey_to_RGB = cv2.cvtColor(grey, cv2.COLOR_GRAY2RGB )

    UV=RBG_to_YUV(img)
    UV[:,:,0]=0
    color_to_RGB=YUV_to_RGB(UV)
    back=grey_to_RGB+color_to_RGB

    imsave(os.path.join(CON_PATH,file_name+'_back_to_color.png'),grey_to_RGB+color_to_RGB)
