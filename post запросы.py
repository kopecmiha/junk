import requests
import time
import json
import base64
import random



lat = 44.725
long = 37.7593
'''
for i in range (100):
    response = requests.get('http://aumsuhere.tmweb.ru/api/db/view_home_by_id/' + str(i))
    if eval(str(response.text)) != {"result":"fail"}:
        data = eval(str(response.text))
        data["type_of_cabel"] = "Витая пара"
        data["type_of_connection"] = "gigabite Etherneth"
        response = requests.get('http://aumsuhere.tmweb.ru/api/db/update_home_router', json = data)
        print(response.text)
'''
for i in range (100):
    response = requests.get('http://aumsuhere.tmweb.ru/api/db/view_by_id/' + str(i))
    if eval(str(response.text)) != {"result":"fail"}:
        data = eval(str(response.text))
        data["type_of_cabel"] = "Витая пара"
        data["type_of_connection"] = "gigabite Etherneth"
        response = requests.get('http://aumsuhere.tmweb.ru/api/db/update_router', json = data)
        print(response.text)
    
'''
for rout in data:
    data2.append({'Type': rout["Type"], 'connect_id': rout["connect_id"], 'inf_count': rout["inf_count"],
                  'model': rout["model"],
                  'on_off': rout["on_off"],
                  'smotr': rout["smotr"]})
for rou in data2:
    response = requests.get('http://aumsuhere.tmweb.ru/api/db/add_home_router', json = rou)
    print(response.text)
'''    
    
    


        
