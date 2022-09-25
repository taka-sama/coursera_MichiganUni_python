# tp = (1, 100, 5) < (1, 233, 4)
# print(bool(tp))


fhand = open('romeo.txt')
counts = dict()
for line in fhand:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.item():
  newtup = 