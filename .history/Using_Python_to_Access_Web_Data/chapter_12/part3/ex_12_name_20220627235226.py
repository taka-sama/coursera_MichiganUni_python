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


def third_url(position):
  tags = soup('a')
  num_position = int(position)
  count = 0
  for tag in tags:
    count += 1
    if count == num_position:
      target_url = tag.get('href', None)
      print(target_url)
  return target_url

# position = input('Enter position:')
position = 3
third_url(position)
    
 unction(input: url, return url number) (
Finds and returns the third url found in the input url
)

main code(
first url=finkret url
url return number=3
returned url = first url
loop(i : 4)(
returned url = function (first url, return number)
print retrieved url name
)