fhand = open('mbox-short.txt')
colon = ':'
count = 0
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
  # print('wspt',wspt)
  hours = wspt[0]
  # print('hours',hours)
  for w in wspt[]:
    print(w)
    count = count + 1
    di[w]  = di.get(w,0) + 1
print('count',count)
    

tmp = list()
for k,v in di.items():
  newt = (k,v)
  tmp.append(newt)

tmp = sorted(tmp, reverse=True)

# print(tmp)
# for v,k in tmp[:3]:
#   print(k,v)