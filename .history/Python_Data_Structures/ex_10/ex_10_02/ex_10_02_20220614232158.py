fhand = open('mbox-short.txt')
di = dict()
for lin in fhand:
  lin = lin.rstrip()
  wds = lin.split()
  for w in wds:
    di[w]  = di.get(w,0) + 1
    
print(di)

tmp = list()
for k,v indi.