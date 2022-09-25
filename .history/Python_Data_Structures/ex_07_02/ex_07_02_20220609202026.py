fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswit("X-DSPAM-Confidence:"):
        continue
    print(line)
print("Done")