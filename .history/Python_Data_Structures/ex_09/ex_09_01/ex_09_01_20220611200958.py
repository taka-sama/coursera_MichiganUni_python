from logging.config import dictConfig


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
  