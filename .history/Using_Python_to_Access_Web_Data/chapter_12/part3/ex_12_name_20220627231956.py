import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
# position = 3 #input()
count = 0
# print(url)

def third_url(position):
  
  for tag in tags:
    count += 1
    if count == position:
      target_url = tag.get('href', None)
      print(target_url)
  return target_url

third_url
    
 