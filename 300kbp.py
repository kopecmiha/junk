from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from PIL import Image
import os
files = os.listdir('D:\загрузки\проги')
s = len(files)
x = 0
for i in range (s):
    if (files[i].find('jpg') > -1) or (files[i].find('jpeg') > -1) or (files[i].find('png') > -1):
        size = int(os.stat(files[i]).st_size / 1024)
        if size > 0:
        	x = x + 1
        	img = Image.open(files[i])
        	wide, high = img.size 
        	res = wide/high 
        	s = 3600
        	max_wide = int((s*res)**(1/2))
        	max_high = int(s/max_wide)
        	resized_img = img.resize((max_wide, max_high), Image.ANTIALIAS)
        	resized_img.save(files[i])
        	size = int(os.stat(files[i]).st_size / 1024)
        	print(x, ' ',size)
        else:
            os.remove(files[i])

