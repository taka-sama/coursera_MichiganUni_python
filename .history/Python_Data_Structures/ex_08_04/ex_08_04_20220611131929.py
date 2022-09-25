# fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
for line in fh:
  # print(line.rstrip())
  words = line.rstrip()
  # print(words)
  stuff = words.split()
print(line)