#Using Python to Access Web Data/week6 

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

url = 'http://py4e-data.dr-chuck.net/comments_1565079.json'
myjson = urllib.request.urlopen(url, context=ctx).read().decode()
info = json.loads(myjson)
count = 0
sum = 0
for item in info["comments"]:
  # print(item['count'])
  sum = sum + item['count']
  count = count + 1
print('count',count)
print('sum',sum)