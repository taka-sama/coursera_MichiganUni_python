import re

hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if not re.search('From:', line):
    print(line)