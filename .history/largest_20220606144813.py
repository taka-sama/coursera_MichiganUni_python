largest_so_far = -1
print('Before', largest_so_far)
while True :
  num = input('Enter a number: ')
  if num == 'done':
    break
  try:
    fval = float(num)
  except:
    print('Invalid')

for the_num in [9, 32, 12, 43, 55]:
  if the_num > largest_so_far:
    largest_so_far = the_num
  print(largest_so_far, the_num)
print('After', largest_so_far)