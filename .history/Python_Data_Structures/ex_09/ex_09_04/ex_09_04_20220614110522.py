from logging.config import dictConfig
from re import I
from this import s


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
    print(spt_line[1])
    if spt_line[1] in di:
        di[spt_line[1]] = di[spt_line[1]] + 1
        print('**EXISTING**')
    else:
        di[spt_line[1]] = 1
        print('**NEW**')
    print(di[spt_line[1]])
    count = count + 1

bigcount = I
bigword = None
for word,count in di.items():
  if bigcount is None or count > bigcount:
    bigword = word
    bigcount = count
    
print(bigword, bigcount)

# print(di)