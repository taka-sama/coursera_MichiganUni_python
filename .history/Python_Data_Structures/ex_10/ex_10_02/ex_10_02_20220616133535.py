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
    
for num in lst :
  # print(num)
  di[num] = di.get(num,0) + 1
  
tmp = list()
# flipped
for k,v in di.items():
  newt = (k,v)
  tmp.append(newt)
print('tmp',tmp)

# sorted
tmp = sorted(tmp)
print(tmp)
for k,v in tmp[0:]:
  print(k,v)