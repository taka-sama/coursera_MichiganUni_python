fhand = open('mbox-short.txt')
di = dict()
for lin in fhand:
  lin = lin.rstrip()
  wds = lin.split()
  for w in wds:
    di[w]  = di.get(w,0) + 1

tmp = list()
for k,v in di.items():
  # print(k,v)
  newt = (v,k)
  tmp.append(newt)
  
print(tmp[:3])
tmp = sorted(tmp, reverse=True)
print('Sorted',tmp[:3])

for v,k in di.items():
  print