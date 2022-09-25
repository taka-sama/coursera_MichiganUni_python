from email.encoders import encode_7or8bit
from importlib.resources import contents
from pyexpat import features
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET
import re
import requests
import lxml.html

from numpy import append

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
xml = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(xml, 'xml')
tags = soup('count')
count = 0
lst = list()
sum = 0
for tag in tags:
  count += 1
  tag = int(tag.string)
  lst.append(tag)
  sum = tags + 0
print(sum)
