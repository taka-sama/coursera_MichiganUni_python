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
  # print(wspt)
  # print(hours)
  lst.append(hours)

  for w in lst:
    # w = wspt[0]
    # di[w]  = di.get(w,0) + 1
    count = count + 1
# print(count)
print(lst)
for num in lst :
  
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