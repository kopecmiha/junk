#!/home/c/cp36696/myenv/bin/python3.4
# -*- coding: utf-8 -*-
import vk_api
import json
import random
import requests

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

hello_list = ["привет", "хай", "здарова", "алло", "салам","бот привет", "бот хай", "бот здарова",]

chat_list = ["сделать", "сайт", "андроид"]

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id' : random.randint(0, 999999999999999999999999999999999)})

def write_msg_chat(peer_id, message):
    vk.method('messages.send', {'peer_id': peer_id, 'message': message,  'random_id' : random.randint(0, 999999999999999999999999999999999)})

def getjson(url, data = None):
    response = requests.get(url, params = data)
    response = response.text
    return response

def hello():
    write_msg(event.object.from_id, "Привет, я - Электронный Вышкарь, сейчас нахожусь не на парах, а в разработке.")

def bazar():
    write_msg(event.object.from_id, "Я - Электронный Вышкарь, слишком тупой шоб понять шо вы сказали.")

def sanya(request, name, surname, ID):
    write_msg("176168354",name + " " + surname + "(id" + str(ID) + "): " + request)

def hello_cht():
    write_msg_chat(event.object.peer_id, "иди нахуй")

def bazar_сht():
    write_msg(event.object.peer_id, "Я - Электронный Вышкарь, слишком тупой шоб понять шо вы сказали.")
      
token = "18ead191403825146d15b43a9d3580cb6b74d7b3dfe726582026b55f0544998b3e06758bad681ac1d0031"
vk = vk_api.VkApi(token=token)

longpoll = VkBotLongPoll(vk, wait=25, group_id='185657212')
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW  and event.object['text']:
              if event.from_user:
                request = event.object['text']
                request = request.lower()
                if hello_list.count(request) > 0:
                    hello()
                else:
                    bazar()
              elif event.from_chat:
                  request = event.object['text']
                  request = request.lower()
                  count = 0
                  for i in range(len(chat_list)):
                      if request.count(chat_list[i]) > 0:
                          count = count + 1
                  if count > 1:
                      info = vk.method('users.get', {'user_ids': event.object.from_id})
                      info = info[0]
                      sanya(request, info["first_name"], info["last_name"], event.object.from_id)
                  elif hello_list.count(request) > 0:
                    hello_cht()
