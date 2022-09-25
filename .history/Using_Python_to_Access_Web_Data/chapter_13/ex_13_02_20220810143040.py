import imp
import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_42.json'
# myjson = urllib.request.urlopen(url, context=ctx).read().decode()
# soup = BeautifulSoup(json, "html.parser")
info = json.loads(myjson) #change json file to a dictionary
# print(len(url))
# print(info)

# print(type(info))
mydumps = json.dumps(info, indent=2)
# print(type(dumps))

count = 0
for item in mydumps:
  name = item['name']
  print('name:', name)
  count += 1
  
print(count)