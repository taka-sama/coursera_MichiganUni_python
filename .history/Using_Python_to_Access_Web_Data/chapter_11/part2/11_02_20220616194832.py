from hashlib import sha1
import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+',x)
# print(y) #['2', '19', '42']
# y = re.findall('[AEIOU]+',x)
# print(y) #[]

x = open('/Applications/programming/coursera_Python for everybody/Using_Python_to_Access_Web_Data/chapter_11/part1/mbox-short.txt')
x = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
# y = re.findall('^From: (\S+@\S+)',x)
print(y) #['stephen.marquard@uct.ac.za']