num = 0
tot = 0.0
while True:
  fval = input('Enter a number: ')
  if fval == 'done':
    break
  num = num + 1
  tot = fval 
  
print(tot,num,tot/num)
  