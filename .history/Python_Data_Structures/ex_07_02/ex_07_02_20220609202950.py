# fname = input("Enter file name: ")
fh = open('mbox-short.txt')
fnum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
    num = len(line)
    print(num)
    print(line[20:27])
    fnumx = line[20:27]
    fnum = float(fnumx)
    
print("Done")