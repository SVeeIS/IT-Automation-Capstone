#!/usr/bin/env python3
#memakai API
from PIL import Image
#memakai file yang ada di sistem
import os

#Iterate through each file in the folder
for file in os.listdir():
  #melakukan tindakan jika nama file diawali denga 'ic_'
  if file.startswith('ic_'):
    im_file = Image.open(file)
    #Rotate the image 90° clockwise
    im_file = im_file.rotate(-90)
    #Resize the image from 192x192 to 128x128
    final_im = im_file.resize((128,128))
    #Save the image to a new folder in .jpeg format
    final_im.convert('RGB').save('/opt/icons/'+file+'.jpeg')
