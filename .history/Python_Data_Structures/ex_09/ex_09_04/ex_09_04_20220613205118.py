from logging.config import dictConfig


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith('From'):
        continue
    spt_line = line.split()
    if w in spt_line[0]:
        


#continueの次、    