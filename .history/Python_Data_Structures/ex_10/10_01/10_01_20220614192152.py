# tp = (1, 100, 5) < (1, 233, 4)
# print(bool(tp))

#------top 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
  newtup = (val, key)
  lst.append(newtup)
  
lst = sorted(lst, reverse=True)
#top10
for val, key in lst[:10]:
  print(key, val)

#------- ↑ short version
# c = {'a':10, 'b':1, 'c':22}
# print(sorted([(v,k) for k,v in c.items()]))
