import re

handle = open('actual_data')
nulist = list()
for line in handle:
  line = line.rstrip()
  if 