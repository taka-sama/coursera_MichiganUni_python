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
        print('**',spt_line[1],di.get(spt_line[1],-99))
        di[spt_line[1]] = di[spt_line[1]] + 1
    else:
        di[spt_line[1]] = 1
    # print(di[spt_line[1]])

# print(di)