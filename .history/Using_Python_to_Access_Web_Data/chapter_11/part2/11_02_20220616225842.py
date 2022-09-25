from hashlib import sha1
import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+',x)
# print(y) #['2', '19', '42']
# y = re.findall('[AEIOU]+',x)
# print(y) #[]

x = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\',x)
# y = re.findall('^From: (\S+@\S+)',x)
print(y) #['stephen.marquard@uct.ac.za']


#spam confidence
# hand = open('mbox-short.txt')
# numlist = list()
# for line in hand:
#   line = line.rstrip()
#   stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) #extract only numbers
#   if len(stuff) != 1:
#     continue
#   print(stuff)
#   num = float(stuff[0])
#   numlist.append(num)
# print('Maximum:', min(numlist))
# print('Maximum:', max(numlist))
# print(len(stuff))