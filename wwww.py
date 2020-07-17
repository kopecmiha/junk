import requests
import urllib.request
url = 'http://www.atlasobscura.com/destinations'
r = requests.post(url)
rr = r.text
countrie = []
x = rr.find('js-row-member')
rr = rr[x:len(rr)]
s = rr.find('things-to-do')
while s > -1:
   s = rr.find('things-to-do')
   ss = rr[s:len(rr)].find('">') + s
   b = rr[s:ss]
   rr = rr[ss:len(rr)]
   countrie.append(b)
#with open(title.replace('/', '-') + '.json', "w") as write_file: 
            #json.dump(data, write_file)
with open('vvv.txt', "w") as write_file: 
            print(*countrie, file=write_file)
