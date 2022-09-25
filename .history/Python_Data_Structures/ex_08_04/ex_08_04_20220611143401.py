# fname = input("Enter file name: ")
from traceback import print_tb


fh = open('romeo.txt')
lst = list()
for line in fh:
  stuff = line.split()
  for w in stuff:
    try:
      lst.append(w)
    except:
      
lst.sort()
print(lst)