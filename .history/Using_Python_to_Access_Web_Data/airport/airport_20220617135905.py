while True:
  p = input('割引前:')
  if p == 'done':
    break
  pf = float(p)
  b = 0.0114 / pf  #0.01497
  print(b)