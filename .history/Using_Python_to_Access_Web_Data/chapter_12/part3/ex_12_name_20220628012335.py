import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')


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

first_url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' # url = input('Enter - ')
position = 3 # position = input('Enter position:')
int_position = int(position)
repeat = 3 # repeat = input('Enter number of repeat:')
num_repeat = repeat - 2
# returned_url = first_url

for i in range(num_repeat):
  retrieved_url = third_url(first_url,position)
  print(retrieved_url)
  first_url = retrieved_url
  next = third_url(first_url,position)
  print(next)
  
  