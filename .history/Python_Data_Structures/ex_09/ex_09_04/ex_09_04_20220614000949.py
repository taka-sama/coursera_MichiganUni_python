from logging.config import dictConfig


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = 0
colon = ':'
di = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    spt_line = line.split()
    if colon in spt_line[0]:
        continue
    if w in di:
        di
    # print(spt_line[1])
    count = count + 1

print(count)