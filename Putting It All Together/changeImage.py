#!/usr/bin/env python3

import os
from PIL import Image

path = 'supplier-data/images/'
		
for image in os.listdir(path):
	if '.tiff' in image and '.' not in image[0]:
		photo = Image.open(path + image).convert("RGB")
		photo.resize((600, 400)).save(path + image.split('.')[0] + '.jpeg' , 'jpeg') #ubah ukuran dan mengganti extention
		photo.close()
