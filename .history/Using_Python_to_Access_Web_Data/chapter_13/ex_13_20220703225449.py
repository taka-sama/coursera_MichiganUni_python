from importlib.resources import contents
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('comments')
list = list()
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    connum = tag.contents[0]
    num = int(connum)
    list.append(num)
    print('converted', num)
    print('Attrs:', tag.attrs)
    print('End------------------')
    
print(sum(list))

    