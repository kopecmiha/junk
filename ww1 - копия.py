import requests
import urllib.request
import urllib
import json
places = []

url = 'http://flask-test.tw1.ru/index.wsgi/salam/aefef'
site = requests.get(url).text
print(site)


