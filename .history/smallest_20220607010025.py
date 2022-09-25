from cgitb import small


smallest = None
print('Before')
for value in [3, 24, 15, 22, 99, 9]:
  if smallest is None:
    smallest = value
  elif value < smallest:
    smallest = value
  print(smallest, value)
print('After')