# fname = input("Enter file name: ")
from traceback import print_tb


fh = open('romeo.txt')
lst = list()
for line in fh:
  # print(line.rstrip())
  words = line.rstrip()
  stuff = words.split()
  # print(stuff)
  lst.append(line)
  print(lst)