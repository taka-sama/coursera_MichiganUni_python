fhand = open('mbox-short.txt')
colon = ':'
di = dict()
for lin in fhand:
  lin = lin.rstrip()
  if not lin.startswith('From'):
    continue
  wds = lin.split()
  if colon in wds[0]:
    continue
  # print(wds[5])
  time = wds[5]
  wspt = time.split(':')
  print(wspt)
  for w in wds[5]:
    di[w]  = di.get(w,0) + 1

tmp = list()
for k,v in di.items():
  newt = (v,k)
  tmp.append(newt)

tmp = sorted(tmp, reverse=True)

for v,k in tmp[:3]:
  # print(k,v)