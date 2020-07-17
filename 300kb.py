#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from PIL import Image
import os
files = ('111.jpg')
img = Image.open(files)
size = int(os.stat(files).st_size / 1024)
width = 100
height = 100
resized_img = img.resize((width, height), Image.ANTIALIAS)
resized_img.save(files)

