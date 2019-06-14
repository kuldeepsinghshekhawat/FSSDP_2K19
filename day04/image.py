# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:04:13 2019

@author: lenovo
"""

from PIL import Image

#os.chdir("/Users/sylvester/Desktop/Python/")

# Open the image and create it's instance
img = Image.open("sample.jpg")

# Gives the dimensions or the size of the image
print (img.size)

# Gives the width of the image
print (img.width)

# Gives the width of the image
print (img.height)


# Gives the format of image like JPEG, PNG ...
print (img.format)

# Gives the mode of image like RGB, binary, GreyScale ...
print (img.mode)

# Displays the Image
img.show()


# Rotate the image with the given angle
# Create separate instance for rotated image
# ROTATE_90, ROTATE_180, ROTATE_270
img_rotate = img.transpose(Image.ROTATE_90)
 
# Displays the rotated image
img_rotate.show()  

img_rotate.save("sample1.jpg")


# Resizing the image 
small_im = img.resize((160, 204), resample=Image.BICUBIC)
small_im.save('small_sample1.jpg')


# Creating Thumbnail
img = Image.open("sample.jpg")
img_1=img.thumbnail((75, 75))
img_1.save("kp111.jpg")