counts = dict()
names = ['joh', 'fred', 'mika', 'fred', 'joh', 'mike']
for name in names:
  if name not in counts:
    counts[name] = 1
  else:
    counts[name] = counts[name] + 1
    