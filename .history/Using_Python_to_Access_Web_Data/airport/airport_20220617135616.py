while True:
  p = input('割引前:')
  if p == 'done':
    break
  pf = float(p)
  b = 0.01497 * pf
  print(b)