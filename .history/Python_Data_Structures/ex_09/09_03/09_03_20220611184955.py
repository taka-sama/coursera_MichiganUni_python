from itertools import count


counts = dict()
fh = open('romeo.txt')
for line in fh:
  for word in words:
    counts[word] = counts.get(word,0) + 1
  words = line.split()
  
print('Words:', words)
print('Counting...')
print('Counts', counts)
  