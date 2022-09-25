# name = input('Enter file:')
# if len(name) < 1:
#   name = 'mbox-short.txt'
name = 'mbox-short.txt'
handle = open(name)
counts = dict()
for line in handle:
  words = line.strip()
  for word in words:
    counts[word] = counts.get(word,0) + 1
    
lst = list()
for key, val in counts.items():
  newtup = 
