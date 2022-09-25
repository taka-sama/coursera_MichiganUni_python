# fname = input("Enter file name: ")
fh = open('mbox-short.txt')
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
    num = len(line)
    print(num)
    print(line[20:27])
    print(line[20:27])
    fnum = float()
print("Done")