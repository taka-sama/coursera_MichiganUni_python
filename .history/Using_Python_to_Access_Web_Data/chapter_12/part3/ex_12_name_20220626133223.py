from turtle import pos, position
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('a')
position_count = 0
position = input('Enter potion:')
fp = float(position)
for tag in tags:
  position_count = count + 1
  if count == fp:
    print('Retrieving:',tag.get('href',None))
    break