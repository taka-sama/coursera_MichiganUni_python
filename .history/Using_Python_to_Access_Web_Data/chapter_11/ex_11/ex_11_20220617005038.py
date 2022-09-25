import re

handle = open('actual_data')
numlist = list()
for line in handle:
  line = line.rstrip()
  stuff = re.findall('[0-9]+', line) #extract only numbers
  if len(stuff) != 1:
    continue
  # print(stuff)
  # num = float(stuff[0])
  # print(num)
  numlist.append(num)
print(sum(numlist))