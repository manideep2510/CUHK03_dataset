import os
import numpy as np
import glob
from scipy.misc import imresize
from scipy.misc import imsave
import matplotlib.pyplot as plt
from PIL import Image
#from skimage import transform


filenamesx = [imgx for imgx in glob.glob('val/*.jpg')]

filenamesx.sort()

i = 1
imagesx = []
imagesx_resized = []
for imgx in filenamesx:
    if not imgx.endswith("superpixels.png" or ".txt"):
        imgsx = plt.imread(imgx)
        imgsx_resize = imresize(imgsx, (160, 60))
        #imgsx_resize = skimage.transform.resize(imgx, (128, 192))
        locals()["imgx"+str(i)] = imgsx_resize
        i = i+1
        print(imgx)
        
"""for i in range(150):
    imagesx_resized.append(locals()["imgx"+str(i+1)])"""


for i in range(938):
	imx = Image.fromarray(locals()["imgx"+str(i+1)])
	# First create a folder named "train"
	imx.save("val_resized/"+ filenamesx[i][4:])
    
