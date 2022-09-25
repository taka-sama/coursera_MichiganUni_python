import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def third_url(url,position):
  url = first_url
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  count = 0
  for tag in tags:
    count += 1
    if count == int_position:
      target_url = tag.get('href', None)
  return target_url

first_url = 'http://py4e-data.dr-chuck.net/known_by_Corie.html' # url = input('Enter - ')
print(first_url)
position = 18 # position = input('Enter position:')
int_position = int(position)
num_repeat = 7

for i in range(num_repeat):
  first_url = third_url(first_url,position)
  print(first_url)