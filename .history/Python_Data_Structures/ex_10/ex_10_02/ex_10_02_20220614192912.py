# name = input('Enter file:')
# if len(name) < 1:
#   name = 'mbox-short.txt'
name = 'mbox-short.txt'
handle = open(name)
counts = dict()
for line in handle:
  line = line.strip()
