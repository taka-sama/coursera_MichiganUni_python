from itertools import count


counts = dict()
lst = list()
fh = open('romeo.txt')
for line in fh:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word,0) + 1
    lst.append(word)
    
print(lst)
print('Words:', lst)
print('Counting...')
print('Counts', counts)
  