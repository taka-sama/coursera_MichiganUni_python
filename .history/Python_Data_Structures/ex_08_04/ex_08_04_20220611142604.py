# fname = input("Enter file name: ")
from traceback import print_tb


fh = open('romeo.txt')
lst = list()
for line in fh:
  # print(line.rstrip())
  stuff = line.split()
  print(stuff)
  lst.append(stuff)
  for w in stuff:
    lst.append(w)
  
# print(lst)