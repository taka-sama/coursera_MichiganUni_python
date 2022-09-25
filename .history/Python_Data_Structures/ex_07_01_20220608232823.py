fname = input('Enter the file name: ')
fname = 'words.txt
try:
  fhand = open(fname)
except:
  print('File cannot open:', fname)
  quit()
# for line in fhand:
readf = fhand.read()
print(readf)
  
