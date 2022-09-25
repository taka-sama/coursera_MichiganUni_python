import re

handle = open('actual_data')
numlist = list()
count = 0
for line in handle:
  line = line.rstrip()
  # print(line)
  stuff = re.findall('[0-9]+', line) #extract only numbers
  print(type(stuff)
  if len(stuff) < 1:
    continue
  # print(stuff)
  for item in stuff:
    numlist.append(float(item))
    count = count + 1
# print(count)