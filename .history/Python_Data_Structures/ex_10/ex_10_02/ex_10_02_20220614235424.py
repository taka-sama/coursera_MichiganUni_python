fhand = open('mbox-short.txt')
di = dict()
for lin in fhand:
  lin = lin.rstrip()
  if not lin.startswith('From'):
    continue
  wds = lin.split()
  if colon in wds
  for w in wds:
    di[w]  = di.get(w,0) + 1

tmp = list()
for k,v in di.items():
  newt = (v,k)
  tmp.append(newt)

tmp = sorted(tmp, reverse=True)

for v,k in tmp[:3]:
  print(k,v)