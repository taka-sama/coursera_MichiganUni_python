import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
  wordss = line.decode().strip()
  words = wordss.strip()
  for word in words:
    counts[word] = counts.get(word,0) + 1
print(counts)