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
  print(lin)
  time = wds[5]
  wspt = time.split(':')
  print('wspt',wspt)
  lst = app
  for w in wspt:
    di[w]  = di.get(w,0) + 1
x = di.items()
print(x)

# tmp = list()
#flipped
# for k,v in di.items():
#   newt = (k,v)
#   tmp.append(newt)

#sorted
# tmp = sorted(tmp, reverse=True)

# print(tmp)
# for v,k in tmp[:3]:
#   print(k,v)