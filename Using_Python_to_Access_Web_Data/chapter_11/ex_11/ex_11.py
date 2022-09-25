import re

handle = open('actual_data')
numlist = list()
count = 0
for line in handle:
  line = line.rstrip()
  # print(line)
  stuff = re.findall('[0-9]+', line) #extract only numbers
  if len(stuff) < 1:
    continue
  
  for item in stuff:
    numlist.append(int(item))
    count = count + 1
# print(len(numlist))
print(sum(numlist))