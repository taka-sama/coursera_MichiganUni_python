# fname = input("Enter file name: ")
from traceback import print_tb


fh = open('romeo.txt')
lst = list()
for line in fh:
  stuff = line.split()
  for w in stuff:
      lst.append(w) in lst
lst.sort()
print(lst)