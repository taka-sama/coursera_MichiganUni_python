import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
  words = line.decode().split()
  for word in words:
    counts[word] = count.get(wor)