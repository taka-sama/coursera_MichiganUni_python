from logging.config import dictConfig


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = 0
w = ':'
for line in handle:
    line = 
    if not line.startswith('From'):
        continue
    spt_line = line.split()
    if w in spt_line[0]:
        continue
    print(spt_line[1])
    count = count + 1

print(count)