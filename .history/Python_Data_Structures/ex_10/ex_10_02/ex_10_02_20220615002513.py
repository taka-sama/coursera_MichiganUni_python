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
  time = wds[5]
  wspt = time.split(':')
  hours = wspt[0]
  # print(hours)
  for w in hours:
    di[w]  = di.get(w,0) + 1
    print(di[w])
    

tmp = list()
for k,v in di.items():
  newt = (v,k)
  tmp.append(newt)

tmp = sorted(tmp, reverse=True)
print(tmp)

# for v,k in tmp[:3]:
#   print(k,v)