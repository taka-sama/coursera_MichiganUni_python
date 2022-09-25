from itertools import count
import json
import imp
import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.json'
myjson = urllib.request.urlopen(url, context=ctx).read().decode()
info = json.loads(myjson)
count = 0
info_values = info["comments"]
for item in info["comments"].values():
  # print(item)
  count = count + 1
  print(item)

print(count)
# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

# info = json.loads(data)
# print('User count:', len(info))
# print('User count:', info)
# count = 0
# sum = 0
# for item in info:
#   print('Name', item['name'])
#   print('Id', item['id'])
#   print('Attribute', item['x'])
#   int_item = int(item['x'])
#   sum = sum + int_item
#   count += 1
# print('count',count)
# print('sum',sum)