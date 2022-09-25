fname = input('Enter the file name: ')
try:
  fhand = open(fname)
except:
  print('File cannot open:', fname)
  quit()
  
