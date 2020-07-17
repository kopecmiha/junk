#!/usr/bin/env python

import requests
import urllib.request
from sys import getdefaultencoding
from bs4 import BeautifulSoup
import urllib
import json
import os
import re
getdefaultencoding()


url_help = 'https://api.hh.ru/specializations'
url = 'https://api.hh.ru/vacancies?specialization='
spec_name_id = requests.get(url_help).text
spec_name_id = json.loads(spec_name_id)
for i in range(len(spec_name_id)):
    spec = spec_name_id[i]["specializations"]
    for j in range(len(spec)):
        ID = spec[j]["id"]
        spec_name = spec[j]["name"]
        points_list = []
        vacancies = requests.get(url + str(ID) + "&per_page=100").text
        vacancies = json.loads(vacancies)
        pages_count = vacancies["pages"]
        for m in range(pages_count):
            vacancies = requests.get(url + str(ID) + "&per_page=100&page=" + str(m)).text
            vacancies = json.loads(vacancies)
            for n in range(len(vacancies["items"])):
                if vacancies["items"][n]["salary"] != None:
                    salary = vacancies["items"][n]["salary"]["from"]
                    currency = vacancies["items"][n]["salary"]["currency"]
                else:
                    salary = None
                if vacancies["items"][n]["name"] != None:
                    vac_name = vacancies["items"][n]["name"]
                    if vacancies["items"][n]["address"] != None:
                        if vacancies["items"][n]["address"]["lat"] != None:
                            lat =  vacancies["items"][n]["address"]["lat"]
                            if vacancies["items"][n]["address"] != None:
                                if vacancies["items"][n]["address"]["lng"] != None:
                                    lng =  vacancies["items"][n]["address"]["lng"]
                                    point = { "type": "Feature","geometry": {"type": "Point", "coordinates": [lng, lat]},"properties": {"specialization name" : spec_name, "vacancy name" : vac_name, "salary" : salary, "currency" : currency}}
                                    points_list.append(point)
        geojson = { "type" : "FeatureCollection","features" : points_list}
        with open(r"D:\загрузки\ooo\hhru" + chr(92) + spec_name.replace("/", "-") + '.geojson', "w") as write_file:
              json.dump(geojson, write_file)


      


