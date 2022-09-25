while True:
  p = input('割引前:')
  if p == 'done':
    break
  pf = float(p) * 1000
  b = 0.011497 / pf  #0.01497
  print(b)