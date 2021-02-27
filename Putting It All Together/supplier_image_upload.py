#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
image_path = 'supplier-data/images/'
list_image = os.listdir(image_path)
jpeg_images = [image_name for image_name in list_image if '.jpeg' in image_name]

for image in jpeg_images:
  with open(image_path + image, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
