# while True:
#   data = mysock.recv(512)
#   if (len(data) < 1):
#     break
#   print(data.decode())

from unicodedata import decimal


words = input('!^')
for myord in words:
  print(ord(myord))