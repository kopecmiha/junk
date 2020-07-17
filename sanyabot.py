#!/home/c/cp36696/myenv/bin/python3.4
# -*- coding: utf-8 -*-
import vk_api
import json
import random
import requests
from vk_api.longpoll import VkLongPoll, VkEventType

hello_list = ["привет", "хай", "здарова", "алло"]

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id' : random.randint(0, 999999999999999999999999999999999)})

def getjson(url, data = None):
    response = requests.get(url, params = data)
    response = response.text
    return response

def hello():
    write_msg(event.user_id, "Привет, я бот.")

def bazar():
    write_msg(event.user_id, "я бот.")

login, password = '79186702834', 'злобныймишка678'
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
    
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:        
            request = event.text
            request = request.lower()
            ID = event.message_id
            if hello_list.count(request) > 0:
                hello()
            else:
                bazar()
            
                
               
            
