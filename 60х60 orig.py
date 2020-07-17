from PIL import Image
import os
width = 800
height = 600
files = os.listdir('D:\загрузки\проги')
s = len(files)
print(s)
for i in range (s):
    if (files[i].find('jpg') > -1) or (files[i].find('png') > -1) or (files[i].find('jpeg') > -1):
        img = Image.open(files[i])
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        resized_img.save(files[i])                

