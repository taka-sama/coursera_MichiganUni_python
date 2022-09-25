from turtle import position
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
count = 0
for tag in tags:
  count = count + 1
  if count == 3:
    print('Retrieving:',tag.get('href',None))
    break
  first_name = tag.get('href',None)
  print(first_name)

sec_url