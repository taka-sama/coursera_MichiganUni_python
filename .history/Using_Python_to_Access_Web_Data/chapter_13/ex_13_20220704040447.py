from email.encoders import encode_7or8bit
from importlib.resources import contents
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET
import re

from numpy import append

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

dec_soup = soup.
stuff = ET.fromstring(soup)