import re

handle = open('actual_data')
numlist = list()
for line in handle:
  line = line.rstrip()
  # print(line)
  stuff = re.findall('[0-9]+', line) #extract only numbers
  # print(stuff)
  if len(stuff) < 1:
    continue
  # print(stuff)python3 ex_11.py
  for item in stuff:
    numlist.append(float(item))
  print(sum(numlist))
    # print(item)
  # num = float(stuff[0])
  # print(num)
#   numlist.append(num)
# print(numlist)
# print(sum(numlist))