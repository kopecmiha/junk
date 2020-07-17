
import requests
import time 
mass=[]
def getjson(url, data = None):
    response = requests.get(url, params = data)
    response = response.text
    return response
access_token = '9026fa36a4a52ad4d8d1101119c490c0cff189e3554111ebdde4455a79932951bd5613859b4504f9430bd'
#owner_id = '121833389'
#count = 120
with open('scr.txt') as f2:
    screen_name = f2.read()

util = getjson("https://api.vk.com/method/utils.resolveScreenName", {
        'screen_name' : screen_name,
        #'count' : count,
        'access_token' : access_token,
        'v' : '5.52'
        })
owner_id = util[util.find('id')+4:len(util)-2]
photos = getjson("https://api.vk.com/method/photos.getAll", {
        'owner_id' : owner_id,
        #'count' : count,
        'access_token' : access_token,
        'v' : '5.52'
        })
user = getjson("https://api.vk.com/method/users.get", {
        'user_ids' : owner_id,
        #'count' : count,
        'access_token' : access_token,
        'v' : '5.52'
        })
wall = getjson("https://api.vk.com/method/wall.get", {
        'owner_id' : owner_id,
        #'count' : count,
        'access_token' : access_token,
        'v' : '5.52'
        })
with open('vv.txt','w', encoding='utf-8') as f3:
    f3.write(user + '\n')
    f3.write('***************************' + '\n')
    f3.write(wall + '\n')
    f3.write('***************************' + '\n')
    f3.write(photos + '\n')

