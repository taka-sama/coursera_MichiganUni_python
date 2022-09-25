fn = input('Enter a file name: ')
fh = open(fn)

for lx in fh:
  ly = lx.rstrip()
  print(ly.upper())