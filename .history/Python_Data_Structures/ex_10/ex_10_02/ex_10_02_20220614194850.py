# name = input('Enter file:')
# if len(name) < 1:
#   name = 'mbox-short.txt'
from tkinter.tix import Tree


name = 'mbox-short.txt'
handle = open(name)
counts = dict()
for line in handle:
  words = line.strip()
  if not 
  for word in words:
    counts[word] = counts.get(word,0) + 1
    
lst = list()
for key, val in counts.items():
  newtup = (val, key)
  lst.append(newtup)
  
lst = sorted(lst, reverse=True)
for val, key in lst[:3]:
  print(key, val)