import requests

url = 'http://admire.social/images-creator/images/1.py'
r = requests.post(url)
rrr = r.text
s = rrr.find('good')
while s == -1:
    r = requests.post(url)
    rrr = r.text
    s = rrr.find('good')
    ss = rrr.rfind('hello')
    print(rrr[ss:ss+25])
print(rrr)
