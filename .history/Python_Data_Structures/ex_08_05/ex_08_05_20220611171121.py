# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"

fh = open('mbox-short.txt')
count = 0
w = ':'
for line in fh:
  if not line.startswith('From'):
    continue
  spt_line = line.split()
  # print(spt_line[1])
  if w in spt_line[0]:
    break
  print(spt_line)
  count = count + 1

print("There were", count, "lines in the file with From as the first word")
