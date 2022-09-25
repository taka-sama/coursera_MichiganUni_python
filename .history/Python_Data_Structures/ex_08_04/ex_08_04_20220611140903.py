# fname = input("Enter file name: ")
from traceback import print_tb


fh = open('romeo.txt')
lst = list()
for line in fh:
  # print(line.rstrip())
  print(line.split())
  lst = line.append()
  
print(lst)