#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib.request
import urllib
from bs4 import BeautifulSoup
from sys import getdefaultencoding
import json

getdefaultencoding()
url = 'http://www.etovidel.net/sights/city'
r = requests.post(url)
rrr = r.text
arr = []
x = rrr.find('/sights/city')
while x > -1: 
   ss = rrr[x:len(rrr)].find('>') + x
   arr.append(rrr[x:ss])
   rrr = rrr[ss:len(rrr)]
   x = rrr.find('/sights/city')

for i in range(len(arr)-3151):
   

   url = 'http://www.etovidel.net' + arr[i+3151][0:len(arr[i+3151])-1]
   r = requests.post(url)
   imag = []
   rr = r.text

   
   s = rr.find('<title>') + 7
   ss = rr.find('</title>')
   title = chr(39) + rr[s:ss] + chr(39)
   tags = title.split(',')
   title = tags[0][1:len(tags[0])]
   if len(tags) > 1:
      tags = tags[1:len(tags)]
      tags[len(tags)-1]=tags[len(tags)-1][0:len(tags[len(tags)-1])-1]
   else:
      tags = []
   if tags.count(' Только что добавлено') > 0:
      tags.remove(' Только что добавлено')
   if tags.count(' Другой город') > 0:
      tags.remove(' Другой город')

   s = rr.find('id='+chr(34)+'mycollection'+chr(34))
   ss = rr[s:len(rr)].find('<script') + s
   desc = rr[s:ss]
   s = desc.find('div') + 4
   ss = desc[s:len(desc)].find('<p>') + s
   desc = desc[s:ss]
   x = desc.find('<br />')
   while x > -1:
      desc = desc[0:x] + '<' + chr(92) + 'n>' + desc[x+6:len(desc)]
      x = desc.find('<br />')
   desc = desc.encode('utf-8')
   description = desc.decode('utf-8')
   true_description = BeautifulSoup(description) 
   for script in true_description(["script", "style"]): 
      script.extract() 
   description = true_description.get_text()
   
   s = rr.find('coords') + 7
   ss = rr[s:len(rr)].find(' ') + s - 1
   cord = rr[s:ss]
   s = cord.find(',')
   route = cord.split(',')
   if len(route) > 1:
      rou = route[0]
      route[0] = route[1]
      route[1] = rou

   rrr = rr
   x = rrr.find('/appended_files/big')
   while x > -1:
      ss = rrr[x:len(rrr)].find('jpg') + x + 3
      ima = 'http://www.etovidel.net' + rrr[x:ss]
      rrr = rrr[ss:len(rrr)]
      imag.append(ima)
      x = rrr.find('/appended_files/big')
      #url = ima
      #img = urllib.request.urlopen(url).read()
      #with open(r'D:/загрузки/ooo/bbb/img' + str(x) + '.jpg', "wb") as out:
         #out.write(img)

   rrr = rr
   x = rrr.find('sights/tag')
   while x > -1:
      x = rrr[x:len(rrr)].find('>') + x + 1
      ss = rrr[x:len(rrr)].find('<') + x
      tags.append(rrr[x:ss])
      rrr = rrr[ss:len(rrr)]
      x = rrr.find('sights/tag')

   if len(imag) > 0:      
      avatar = imag[0].replace('big','mid0')
   else:
      avatar = ' '
   url = "https://admire.social/back/add-place-other.php"
   data = {
           'title' : title,
           'description' : description,
           'images' : imag,
           'tags' : tags,
           'avatar' : avatar,
           'route' : route
           }
   with open(title.replace('/', '-') + '.json', "w") as write_file: 
        json.dump(data, write_file)

