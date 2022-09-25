from multiprocessing.sharedctypes import Value


largest_so_far = -1
smallest_so_far = None
while True :
  num = input('Enter a number: ')
  if num == 'done':
    break
  try:
    fval = int(num)
  except:
    print('Invalid input')
    continue
  if fval > largest_so_far:
    largest_so_far = fval
  if smallest_so_far is None:
    smallest_so_far = fval
  elif fval < smallest_so_far:
    smallest_so_far = fval
  
print('Maximum is',largest_so_far)
print('Minimum is',smallest_so_far)