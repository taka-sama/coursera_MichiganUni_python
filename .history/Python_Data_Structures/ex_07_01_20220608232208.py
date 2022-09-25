fname = input('Enter the file name: ')
try:
  fhand = open('words.txt')
except:
  print('File cannot open:', fname)
  quit()
# for line in fhand:
readf = fhand.read()
print(readf)
  
