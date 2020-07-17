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
owner_id = '121833389'
#count = 120 


all_posts=[]


photos = getjson("https://api.vk.com/method/photos.getAll", {
        'owner_id' : owner_id,
        #'count' : count,
        'access_token' : access_token,
        'v' : '5.52'
        })

friends = getjson("https://api.vk.com/method/friends.get", {
        'owner_id' : owner_id,
        #'count' : count,
        'access_token' : access_token,
        'v' : '5.52'
        })
s = photos.find(chr(92))
while s > -1:
    s = photos.find(chr(92))
    if s > -1:
        photos = photos[0:s] + photos[s+1:len(photos)]
ss = photos.find('https')
while ss > -1:
    ss = photos.find('https')
    sj = photos.find('jpg')
    mass.append(photos[ss:sj+3])
    photos = photos[sj+4:len(photos)]
print(mass)
