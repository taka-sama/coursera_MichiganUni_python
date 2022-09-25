# fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
print(fh)
for line in fh:
  # print(line.rstrip())
  stuff = line.split()
  print(stuff)