import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    # +1 734 303 4456
    2002-05-30T09:30:10Z
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('phone'))
print('Attr:', tree.find('email').get('hide'))
