import re

handle = open('actual_data')
nulist = list()
for line in handle:
  line = line.rstrip()
  stuff = re.findall('([0-9.]+)', line) #extract only numbers
  if len(stuff) != 1:
    continue
  if []
  print(stuff)