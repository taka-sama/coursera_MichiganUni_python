# fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
stuff = fh.split()
for line in fh:
  print(line.rstrip())