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
    if count == :
      target_url = tag.get('href', None)
      print(target_url)
  return target_url

first_url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' # url = input('Enter - ')
position = 3 # position = input('Enter position:')
int_position = int(position)
num_repeat = 4 # num_repeat = input('Enter number of repeat:')

third_url(first_url,position)
returned_url = first_url
print(returned_url)

for i in len(num_repeat):