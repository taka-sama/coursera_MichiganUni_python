largest_so_far = -1
print('Before', largest_so_far)
num = input('Enter a number: ')
for the_num in [9, 32, 12, 43, 55]:
  if the_num > largest_so_far:
    largest_so_far = the_num
  print(largest_so_far, the_num)
print('After', largest_so_far)