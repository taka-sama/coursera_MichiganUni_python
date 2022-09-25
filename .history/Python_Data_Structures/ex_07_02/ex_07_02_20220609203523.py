# fname = input("Enter file name: ")
fh = open('mbox-short.txt')
fallnum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # print(line)
    num = len(line)
    # print(num)
    print(line[20:27])
    fnumx = line[20:27]
    fnum = float(fnumx)
    fallnum = fallnum + fnum
    count = count + 1
    average = fallnum / count
    
print(fallnum)
print(average)
print("Done")