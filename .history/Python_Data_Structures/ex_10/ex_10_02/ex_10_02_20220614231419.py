fhand = open('mbox-short.txt')
for lin in fhand:
  lin = lin.rstrip()
  wds = lin.split()
  for w in wds:
    di[w]  = di.get(w,0) 