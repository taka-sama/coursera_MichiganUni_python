fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
    num = len(line)
    print(num)
    print(linembox-short.txt
          [22:27])
print("Done")