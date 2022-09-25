while True:
  p = input('旅客数:')
  if p == 'done':
    break
  pf = float(p)
  b = 0.014 * pf
  print(b)