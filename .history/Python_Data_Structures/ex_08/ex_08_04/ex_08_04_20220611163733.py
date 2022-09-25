# fname = input("Enter file name: ")
from traceback import print_tb


fh = open('romeo.txt')
lst = list()
for line in fh:
  stuff = line.split()
  for w in stuff:
    if w not in lst:
      lst.append(w)
lst.sort()
print(lst)