from curses.ascii import ETB
from tkinter.tix import Tree
from xml.dom.minidom import Element
import xml.etree.ElementTree as ET

from numpy import fromstring

data = '''<person>
  <name>Chuck</name>
  <phone type="intl"> 
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))