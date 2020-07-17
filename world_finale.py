import requests
import urllib.request
from sys import getdefaultencoding
from bs4 import BeautifulSoup
import urllib
import json
import os
m = 0
getdefaultencoding()

countrie = os.listdir(r"D:\загрузки\ooo\ттт")
for j in range(len(countrie)):
   with open(r"D:\загрузки\ooo\ттт" + chr(92) + countrie[j], "r") as write_file:
    s = write_file.read()
    places = s.split(' ')
   for i in range(len(places)-1):
     url = 'http://www.atlasobscura.com' + places[i]
     my_page = requests.post(url)
     my_page_text = my_page.text


     my_cut_desc = my_page_text.find('<div id="place-body" class="item-body">')   #режем описание 
     ss = my_page_text[my_cut_desc : len(my_page_text)].find('</p>') + my_cut_desc    
     desc = (my_page_text[my_cut_desc:ss]).replace('<div id="place-body" class="item-body">', '').replace('&amp;', '&').replace('&#39;', "'") 
     true_description = BeautifulSoup(desc) 
     for script in true_description(["script", "style"]): 
         script.extract() 
     desc = true_description.get_text()
     #print(desc) 

           
     my_cut_title = my_page_text.find('data-place-title="')   #режем заголовок 
     ss = my_page_text[my_cut_title : len(my_page_text)].find('" data-place-id') + my_cut_title    
     title = (my_page_text[my_cut_title:ss]).replace('data-place-title="', '').replace('&amp;', '&').replace('&#39;', "'")
     #print(title) 




     my_cut_coords = my_page_text.find('<div id="lat-lng-element" class="hidden-sm hidden-xs">')   #режем координаты 
     ss = my_page_text[my_cut_coords : len(my_page_text)].find('<div id="place-map-container" class="item-map-container">') + my_cut_coords    
     coords = (my_page_text[my_cut_coords:ss]).replace('<div id="lat-lng-element" class="hidden-sm hidden-xs">', '').replace('\n', '').replace('</div><div>', ' ').replace('<div>', '').replace('</div></div>', '')
     route = coords.split(' ')
     #print(route)

     my_cut_tags = my_page_text.find("var tagList = '")   #режем теги
     ss = my_page_text[my_cut_tags : len(my_page_text)].find("';") + my_cut_tags    
     tags_str = (my_page_text[my_cut_tags:ss]).replace("var tagList = '", "")
     tags = tags_str.split(';')
     tags.append(countrie[j].replace('.txt', ''))
     #print(tags)

     images = [] #фотки

     my_cut_images = my_page_text.find('class="js-trigger-lightbox gallery-image-container" data-lightbox-src="')   #режем фотки
     while my_cut_images > - 1:  #вырезаем ссылки 
             ss = my_page_text[my_cut_images : len(my_page_text)].find('" data-img') + my_cut_images    
             image = (my_page_text[my_cut_images:ss]).replace('class="js-trigger-lightbox gallery-image-container" data-lightbox-src="', '')
             images.append(image)
             my_page_text = my_page_text[ss:len(my_page_text)]
             my_cut_images = my_page_text.find('class="js-trigger-lightbox gallery-image-container" data-lightbox-src="')

     if len(images) > 0:
         avatar = images[0].replace('big','mid0')
     else:
         avatar = ' '



     data = {
            'title' : title,
            'description' : desc,
            'images' : images,
            'tags' : tags,
            'avatar' : avatar,
            'route' : route
            }
     
     with open(r"D:\загрузки\ooo\iii" + chr(92) + title.replace('/', '-') + '.json', "w") as write_file: 
         json.dump(data, write_file)
