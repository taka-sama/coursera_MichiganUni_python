from curses.ascii import ETB
from tkinter.tix import Tree
from xml.dom.minidom import Element
import xml.etree.ElementTree as ET

data = '''<person>
  <name>Chuck</name>
  <phone type="intl"> 
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>'''