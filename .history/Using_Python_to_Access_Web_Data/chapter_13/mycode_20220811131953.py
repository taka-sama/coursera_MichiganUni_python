from itertools import count
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))
count = 0
int_item = int(item['x'])
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
    print(int_item)
    # sum = int_item + int_item
    count += 1
print('count',count)
# print('sum',sum)