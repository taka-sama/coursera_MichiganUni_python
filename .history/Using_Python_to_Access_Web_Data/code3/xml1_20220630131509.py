import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    # +1 734 303 4456
    May 30, 2002
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name'))
print('Attr:', tree.find('email').get('hide'))
