import requests
import urllib.request
import time
with open(r"usa.txt","r") as write_file:
    s = write_file.read()
    places = s.split(' ')
print(len(places))
