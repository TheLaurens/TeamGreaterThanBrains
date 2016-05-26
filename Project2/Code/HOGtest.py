# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:31:04 2016

Extract Histogram of Oriented Gradients (HOG) for a given image.
The resulting histogram is saved in fd as a vector

@author: roosv_000
"""

import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.feature import hog
from skimage import color, exposure


img = imread('img_94.jpg')
image = color.rgb2gray(img)


fd, hog_image = hog(image, orientations=9, pixels_per_cell=(10, 10),
                    cells_per_block=(1,1), visualise=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input image')
ax1.set_adjustable('box-forced')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))

ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
ax1.set_adjustable('box-forced')
plt.show()