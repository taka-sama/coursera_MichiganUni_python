fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
  if not line.startswith('From'):
    continue
  spt_line = line.split()
  count = count + 1

spt
print("There were", count, "lines in the file with From as the first word")
