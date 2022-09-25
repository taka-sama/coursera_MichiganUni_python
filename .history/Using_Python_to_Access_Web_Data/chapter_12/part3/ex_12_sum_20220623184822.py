# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from importlib.resources import contents
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_1565076.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')

for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    connum = tag.contents[0]
    num = int(connum)
    # y = sum(num)
    # print(sum(num))
    print('converted', num)
    print('Attrs:', tag.attrs)
    print('End------------------')
    