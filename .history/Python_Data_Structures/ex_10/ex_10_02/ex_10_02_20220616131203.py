fhand = open('mbox-short.txt')
colon = ':'
count = 0
lst = list()
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
  lst.append(hours)
  for w in wspt:
    w = wspt[0]
    # di[w]  = di.get(w,0) + 1
  count = count + 1
print(di)
print(count)
tmp = list()
# flipped
for k,v in di.items():
  newt = (k,v)
  tmp.append(newt)

# sorted
tmp = sorted(tmp, reverse=True)

# print(tmp)
# for v,k in tmp[0:]:
#   print(k,v)