from ast import Num


num = 0
tot = 0.0
while True :
  sval = input('Enter a number: ')
  if sval == 'done':
    break
  try:
    fval = float(sval)
  except:
    print('Invalid input')
    continue
  largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 32, 12, 43, 55]:
  if the_num > largest_so_far:
    largest_so_far = the_num
  num = num + 1
  tot = tot + fval
  
print(tot,num,tot/num)