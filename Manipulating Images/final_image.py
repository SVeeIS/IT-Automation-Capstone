#!/usr/bin/env python3
#memakai API
from PIL import Image
#memakai file yang ada di sistem
import os

#cek file yang ada di folder
for file in os.listdir():
 
  #melakukan tindakan jika nama file diawali denga 'ic_'
  if file.startswith('ic_'):
    im_file = Image.open(file)
    #rotate image 90 derajat searaj jarum jam -90 /270
    im_file = im_file.rotate(-90)
    #mengubah ukuran image
    final_im = im_file.resize((128,128))
    #simpan ke folder
    final_im.convert('RGB').save('/opt/icons/'+file+'.jpeg')
