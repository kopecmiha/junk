#pip install requests 
#&v=5.52 
#mykey = open(vk_api_key.txt", 'r').read()
#htttps://api.vk.com/method/users.get?user_id=1$v=5.52
#Cdz8TkCn8VwafNvgTFjY ключ
#264bd31a73f5e635a0e5d62c5497a481f44e1835c74594c2c4e5bef42a3b6ecbf8e414782a9ff43ee897a токен
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
screen_name = 'gromozeka2018'

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
        'count' : 20,
        'access_token' : access_token,
        'v' : '5.52'
        })
ss = wall.find('#')
while ss > -1:
        ss = wall.find('#')
        sj = wall[ss:len(wall)].find(' ') + ss
        ssj = 
        print(wall[ss:sj])
        mass.append(wall[ss:sj])
        wall = wall[sj:len(wall)]       
print(mass)

