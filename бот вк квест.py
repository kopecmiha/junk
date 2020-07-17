#!/home/c/cp36696/myenv/bin/python3.4
# -*- coding: utf-8 -*-
import vk_api
import json
import random
import requests
from vk_api.longpoll import VkLongPoll, VkEventType

hello_list = ["Привет", "привет", "хай", "Хай", "здарова", "Здарова", "Алло", "алло"]

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id' : random.randint(0, 999999999999999999999999999999999)})

def write_msg_p(user_id, message, phot):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'attachment' : phot, 'random_id' : random.randint(0, 999999999999999999999999999999999)})

def getjson(url, data = None):
    response = requests.get(url, params = data)
    response = response.text
    return response

def org():
        write_msg(event.user_id, "Разарботчики обновляют приложение, sorry for waiting")
	#write_msg(event.user_id, "Выберите тип квеста")
	#write_msg(event.user_id, "Корпоратив, Детский день рождения, Взрослый день рождения")

def org_hard():
    write_msg(event.user_id, "Выберите сложность")
    write_msg(event.user_id, "Легкий, Средний, Сложный")

def org_time():
    write_msg(event.user_id, "Выберите время прохождения")
    write_msg(event.user_id, "30 минут, 60 минут, 90 минут, Свой вариант")

def org_time_svoi():
    write_msg(event.user_id, "Введите время в минутах")
    
def org_place():
    write_msg(event.user_id, "Передайте геолокацию примерного места проведения и напишите команду ГЕО")

def org_rad():
    write_msg(event.user_id, "Введите радиус вокруг места проведения")

def task_lock():
    write_msg(event.user_id, "Скиньте геолокацию с командой \"Задание\" и свой ID через пробел")

def uchastnic():
    write_msg(event.user_id, "Введите ID")

def get_cord(ID):
    msg = getjson("https://api.vk.com/method/messages.getById", {
         'message_ids' : ID,
         'access_token' : token,
         'v' : '5.101'
         })
    msg = json.loads(msg)
    #msg = msg[msg.find("[") + 1 :msg.rfind("]")]
    msg = msg["response"]
    msg = msg["items"]
    msg = msg[0]["geo"]
    msg = msg["coordinates"]
    task_lat = msg["latitude"]
    task_long = msg['longitude']
    return task_lat,task_long
    #write_msg(event.user_id, str(lat,long))
    #org_rad()

def get_cord2(ID):
    org_rad()


det_plosch = {"long" : 39.183757805767, "lat" : 44.007901950607}
stlov = {"long" : 39.182944533998, "lat" : 44.007990457593}
kuril = {"long" : 39.182385375614, "lat" : 44.007900118623}
vol_girl = {"long" : 39.182140487319, "lat" : 44.008013812548}
security = {"long" : 39.182859605678, "lat" : 44.008428520106}
paradise = {"long" : 39.182517647262, "lat" : 44.008419917455}
pushkin = {"long" : 39.183801405734, "lat" : 44.008563344871}
pen = {"long" : 39.183197798777, "lat" : 44.008140654973}
mayak = {"long" : 39.183666388749, "lat" : 44.008224352599}


ids = ["ID_402_ExpertHere","ID_437_JustCreateIT","ID_789_ConceptMakers","ID_475_TeamNumber7","ID_575_BurevestnicLife","ID_977_Yigdrassil","ID_231_SuperHeres"]
tracks = [{},{},{},{},{},{},{}]
tracks[0] = {"ID" : "ID_402ExpertHere",
             "Stage" : 1,
             "Place1Task" : "Workshop'ы, workshop'ами , а обед по расписанию",
             "Place2Task" : "1) • - - • \n 2) • - \n 3) - - \n 4) • - • - \n 5) - \n 6) - • \n 7) • • \n 8) - • - \n 9) - - • • \n 10) - - - \n 11) • • • - \n 12) • • -",
             "Place3Task" : "Прочитайте с выражением, кто автор? \n 2 46 38 1 \n 116 14 20! \n 15 14 21 \n 14 0 17.",
             "Place4Task" : "Какой чудесный день, \n Какой чудесный ..., \n Какой чудесный я, \n  И песенка моя",
             "Place5Task" : "Вор, разбойник и карманник, \n Берегитесь! Я - ...",
             "Place6Task" : "- Скажи-ка, Саныч, ведь не даром \n С утра мы пахнем перегаром ...",
             "Place1" : stlov,
             "Place2" : vol_girl,
             "Place3" : mayak,
             "Place4" : pen,
             "Place5" : security,
             "Place6" : paradise}

tracks[1] = {"ID" : "ID_437JustCreateIT",
             "Stage" : 1,
             "Place1Task" : "Вор, разбойник и карманник, \n Берегитесь! Я - ...",
             "Place2Task" : "Workshop'ы, workshop'ами , а обед по расписанию",
             "Place3Task" : "Прочитайте с выражением, кто автор? \n 2 46 38 1 \n 116 14 20! \n 15 14 21 \n 14 0 17.",
             "Place4Task" : "Ыъмнфяа Пурёяыфя Шифр Атабаш",
             "Place5Task" : "Там дымят как паровозы, \n Ну, а рядом вянут розы",
             "Place6Task" : "- Скажи-ка, Саныч, ведь не даром \n С утра мы пахнем перегаром ...",
             "Place1" : security,
             "Place2" : stlov,
             "Place3" : mayak,
             "Place4" : det_plosch,
             "Place5" : kuril,
             "Place6" : paradise}

tracks[2] = {"ID" : "ID_789ConceptMakers",
             "Stage" : 1,
             "Place1Task" : "Там дымят как паровозы, \n Ну, а рядом вянут розы",
             "Place2Task" : "Прочитайте с выражением, кто автор? \n 2 46 38 1 \n 116 14 20! \n 15 14 21 \n 14 0 17.",
             "Place3Task" : "Workshop'ы, workshop'ами , а обед по расписанию",
             "Place4Task" : "1) • - - • \n 2) • - \n 3) - - \n 4) • - • - \n 5) - \n 6) - • \n 7) • • \n 8) - • - \n 9) - - • • \n 10) - - - \n 11) • • • - \n 12) • • -",
             "Place5Task" : "Какой чудесный день, \n Какой чудесный ..., \n Какой чудесный я, \n  И песенка моя",
             "Place6Task" : "- Скажи-ка, Саныч, ведь не даром \n С утра мы пахнем перегаром ...",
             "Place1" : kuril,
             "Place2" : mayak,
             "Place3" : stlov,
             "Place4" : vol_girl,
             "Place5" : pen,
             "Place6" : paradise}

tracks[3] = {"ID" : "ID_475TeamNumber7",
             "Stage" : 1,
             "Place1Task" : "Ыъмнфяа Пурёяыфя Шифр Атабаш",
             "Place2Task" : "Вор, разбойник и карманник, \n Берегитесь! Я - ...",
             "Place3Task" : "Там дымят как паровозы, \n Ну, а рядом вянут розы" ,
             "Place4Task" : "Workshop'ы, workshop'ами , а обед по расписанию",
             "Place5Task" : "Прочитайте с выражением, кто автор? \n 2 46 38 1 \n 116 14 20! \n 15 14 21 \n 14 0 17.",
             "Place6Task" : "- Скажи-ка, Саныч, ведь не даром \n С утра мы пахнем перегаром ...",
             "Place1" : det_plosch,
             "Place2" : security,
             "Place3" : kuril,
             "Place4" : stlov,
             "Place5" : mayak,
             "Place6" : paradise}

tracks[4] = {"ID" : "ID_575BurevestnicLife",
             "Stage" : 1,
             "Place1Task" : "1) • - - • \n 2) • - \n 3) - - \n 4) • - • - \n 5) - \n 6) - • \n 7) • • \n 8) - • - \n 9) - - • • \n 10) - - - \n 11) • • • - \n 12) • • -",
             "Place2Task" : "Workshop'ы, workshop'ами , а обед по расписанию",
             "Place3Task" : "Прочитайте с выражением, кто автор? \n 2 46 38 1 \n 116 14 20! \n 15 14 21 \n 14 0 17.",
             "Place4Task" : "Вор, разбойник и карманник, \n Берегитесь! Я - ...",
             "Place5Task" : "Там дымят как паровозы, \n Ну, а рядом вянут розы",
             "Place6Task" : "- Скажи-ка, Саныч, ведь не даром \n С утра мы пахнем перегаром ...",
             "Place1" : vol_girl,
             "Place2" : stlov,
             "Place3" : mayak,
             "Place4" : security,
             "Place5" : kuril,
             "Place6" : paradise}

tracks[5] = {"ID" : "ID_977Yigdrassil",
             "Stage" : 1,
             "Place1Task" : "Прочитайте с выражением, кто автор? \n 2 46 38 1 \n 116 14 20! \n 15 14 21 \n 14 0 17.",
             "Place2Task" : "Какой чудесный день, \n Какой чудесный ..., \n Какой чудесный я, \n  И песенка моя",
             "Place3Task" : "Там дымят как паровозы, \n Ну, а рядом вянут розы",
             "Place4Task" : "Вор, разбойник и карманник, \n Берегитесь! Я - ...",
             "Place5Task" : "Workshop'ы, workshop'ами , а обед по расписанию",
             "Place6Task" : "- Скажи-ка, Саныч, ведь не даром \n С утра мы пахнем перегаром ...",
             "Place1" : pushkin,
             "Place2" : pen,
             "Place3" : kuril,
             "Place4" : security,
             "Place5" : stlov,
             "Place6" : paradise}

tracks[6] = {"ID" : "ID_231SuperHeres",
             "Stage" : 1,
             "Place1Task" : "Какой чудесный день, \n Какой чудесный ..., \n Какой чудесный я, \n  И песенка моя",
             "Place2Task" : "Прочитайте с выражением, кто автор? \n 2 46 38 1 \n 116 14 20! \n 15 14 21 \n 14 0 17.",
             "Place3Task" : "Вор, разбойник и карманник, \n Берегитесь! Я - ...",
             "Place4Task" : "Там дымят как паровозы, \n Ну, а рядом вянут розы",
             "Place5Task" : "Workshop'ы, workshop'ами , а обед по расписанию",
             "Place6Task" : "- Скажи-ка, Саныч, ведь не даром \n С утра мы пахнем перегаром ...",
             "Place1" : pen,
             "Place2" : mayak,
             "Place3" : security,
             "Place4" : kuril,
             "Place5" : stlov,
             "Place6" : paradise}

organisators = []
uchastnics = []

def org_team():
    write_msg(event.user_id, "Выберите количество команд от 1 до 8")

def hello():
    write_msg(event.user_id, "Привет! Я - КвестоБот, первый в мире Робот, создающий квесты. \nТы хочешь создать квест? - Напиши \"Хочу\". \nУчаствуешь в квесте? - напиши \"Участвую\".")

def uch_start(ID):
    if ids.count(ID) > 0:
        check_stage(ID)
    else:
        write_msg(event.user_id, "некорректный ID")

def uch_stage_check(ID,lat_cord,long_cord):
    if tracks[ids.index(ID)]['Stage'] == 1:
        if (lat_cord - tracks[ids.index(ID)]['Place1']['lat']) > -0.00011 and (lat_cord - tracks[ids.index(ID)]['Place1']['lat']) < 0.00011:
            if (long_cord - tracks[ids.index(ID)]['Place1']['long']) > -0.00011 and (long_cord - tracks[ids.index(ID)]['Place1']['long']) < 0.00011:
                tracks[ids.index(ID)]['Stage'] = tracks[ids.index(ID)]['Stage'] + 1
                check_stage(ID)
            else:
                write_msg(event.user_id, "неправильно")
                task_lock()
        else:
            write_msg(event.user_id, "неправильно")
            task_lock()
    if tracks[ids.index(ID)]['Stage'] == 2:
        if (lat_cord - tracks[ids.index(ID)]['Place2']['lat']) > -0.00011 and (lat_cord - tracks[ids.index(ID)]['Place2']['lat']) < 0.00011:
            if (long_cord - tracks[ids.index(ID)]['Place2']['long']) > -0.00011 and (long_cord - tracks[ids.index(ID)]['Place2']['long']) < 0.00011:
                tracks[ids.index(ID)]['Stage'] = tracks[ids.index(ID)]['Stage'] + 1
                check_stage(ID)
            else:
                write_msg(event.user_id, "неправильно")
                task_lock()
        else:
            write_msg(event.user_id, "неправильно")
            task_lock()
    if tracks[ids.index(ID)]['Stage'] == 3:
        if (lat_cord - tracks[ids.index(ID)]['Place3']['lat']) > -0.00011 and (lat_cord - tracks[ids.index(ID)]['Place3']['lat']) < 0.00011:
            if (long_cord - tracks[ids.index(ID)]['Place3']['long']) > -0.00011 and (long_cord - tracks[ids.index(ID)]['Place3']['long']) < 0.00011:
                tracks[ids.index(ID)]['Stage'] = tracks[ids.index(ID)]['Stage'] + 1
                check_stage(ID)
            else:
                write_msg(event.user_id, "неправильно")
                task_lock()
        else:
            write_msg(event.user_id, "неправильно")
            task_lock()
    if tracks[ids.index(ID)]['Stage'] == 4:
        if (lat_cord - tracks[ids.index(ID)]['Place4']['lat']) > -0.00011 and (lat_cord - tracks[ids.index(ID)]['Place4']['lat']) < 0.00011:
            if (long_cord - tracks[ids.index(ID)]['Place4']['long']) > -0.00011 and (long_cord - tracks[ids.index(ID)]['Place4']['long']) < 0.00011:
                tracks[ids.index(ID)]['Stage'] = tracks[ids.index(ID)]['Stage'] + 1
                check_stage(ID)
            else:
                write_msg(event.user_id, "неправильно")
                task_lock()
        else:
            write_msg(event.user_id, "неправильно")
            task_lock()
    if tracks[ids.index(ID)]['Stage'] == 5:
        if (lat_cord - tracks[ids.index(ID)]['Place5']['lat']) > -0.00011 and (lat_cord - tracks[ids.index(ID)]['Place5']['lat']) < 0.00011:
            if (long_cord - tracks[ids.index(ID)]['Place5']['long']) > -0.00011 and (long_cord - tracks[ids.index(ID)]['Place5']['long']) < 0.00011:
                tracks[ids.index(ID)]['Stage'] = tracks[ids.index(ID)]['Stage'] + 1
                check_stage(ID)
            else:
                write_msg(event.user_id, "неправильно")
                task_lock()
        else:
            write_msg(event.user_id, "неправильно")
            task_lock()
    if tracks[ids.index(ID)]['Stage'] == 6:
        if (lat_cord - tracks[ids.index(ID)]['Place6']['lat']) > -0.00011 and (lat_cord - tracks[ids.index(ID)]['Place6']['lat']) < 0.00011:
            if (long_cord - tracks[ids.index(ID)]['Place6']['long']) > -0.00011 and (long_cord - tracks[ids.index(ID)]['Place6']['long']) < 0.00011:
                tracks[ids.index(ID)]['Stage'] = tracks[ids.index(ID)]['Stage'] + 1
                check_stage(ID)
            else:
                write_msg(event.user_id, "неправильно")
                task_lock()
        else:
            write_msg(event.user_id, "неправильно")
            task_lock()
                
                
    
    

def check_stage(ID):
    if tracks[ids.index(ID)]['Stage'] == 1: 
        write_msg(event.user_id, tracks[ids.index(ID)]['Place1Task'])
        task_lock()
    if tracks[ids.index(ID)]['Stage'] == 2: 
        write_msg(event.user_id, tracks[ids.index(ID)]['Place2Task'])
        task_lock()
    if tracks[ids.index(ID)]['Stage'] == 3: 
        write_msg(event.user_id, tracks[ids.index(ID)]['Place3Task'])
        task_lock()
    if tracks[ids.index(ID)]['Stage'] == 4: 
        write_msg(event.user_id, tracks[ids.index(ID)]['Place4Task'])
        task_lock()
    if tracks[ids.index(ID)]['Stage'] == 5: 
        write_msg(event.user_id, tracks[ids.index(ID)]['Place5Task'])
        task_lock()
    if tracks[ids.index(ID)]['Stage'] == 6: 
        write_msg(event.user_id, tracks[ids.index(ID)]['Place6Task'])
        task_lock()
    if tracks[ids.index(ID)]['Stage'] == 7:
        write_msg(event.user_id, "Поздравляю вы прошли")


def org_end(team):
    write_msg(event.user_id, "Ваш квест готов! \n ID Команд-участников: \n ID_402_ExpertHere \n ID_437_JustCreateIT \n ID_789_ConceptMakers\n ID_475_TeamNumber7 \n ID_575_BurevestnicLife \n ID_977_Yigdrassil \n ID_231_SuperHeres \n")
##    if ord(team[0])>=65 and ord(team[0])<= 122:
##        teamID = "ID_" + str(random.randint(0, 2000)) + team
##    else:
##        teamID = "ID_" + str(random.randint(0, 2000)) + transliterate.translit(team, reversed=True)
##    write_msg(event.user_id, teamID)

token = "1b1e3a491bf270d2711ee7ee81407a68e6a561f8bac6dc6509d337ac646ba00101f59b7b028abc20c97ff"
vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk, wait=25, mode=234, preload_messages=True, group_id='186273393')

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:        
            request = event.text
            ID = event.message_id
            if hello_list.count(request) > 0:
                hello()
            elif request == "Хочу":
                org()
                organisators.append(event.user_id)
            elif request == "Участвую":
               uchastnic()
               uchastnics.append(event.user_id)
            elif request == "Корпоратив" or request == "Детский день рождения" or request == "Взрослый день рождения":
               org_hard()
            elif request == "Легкий" or request == "Средний" or request == "Сложный":
               org_time()
            elif request == "ГЕО":
               get_cord2(ID)
            elif request == "Свой вариант":
               org_time_svoi()
            elif request.find("минут")> -1:
                org_place()
            elif request.find("км") > -1:
                org_team()
            elif request.find("команд") > -1:
                org_end(request[request.find(":") + 2:len(request)])
            elif request.find("ID") == 0:
                uch_start(request)
            elif request.find("Задание") == 0:
                task_id = request[8:len(request)]
                lat_cord,leng_cord = get_cord(ID)
                uch_stage_check(task_id,lat_cord,leng_cord)
                
               
            
