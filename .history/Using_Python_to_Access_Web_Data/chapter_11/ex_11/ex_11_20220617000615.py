import re

handle = open('actual_data')
nulist = list()
for line in handle:
  line = line.rstrip()
  if len(stuff) != 1:
    continue
  stuff = re.findall('([0-9.]+)', line) #extract only numbers
  print(stuff)