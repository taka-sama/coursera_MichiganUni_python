from logging.config import dictConfig
from re import I
from this import s


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

colon = ':'
di = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    spt_line = line.split()
    if colon in spt_line[0]:
        continue
    di[spt_line[1]] = di.get(spt_line[1],0) + 1
    bigcount = None
    bigword = None
    for word, count in di.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
        print(,bigcount)

print(di)