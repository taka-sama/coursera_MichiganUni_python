# from itertools import count
#part1

# counts = dict()
# lst = list()
# fh = open('romeo.txt')
# for line in fh:
#   words = line.split()
#   for word in words:
#     counts[word] = counts.get(word,0) + 1
#     lst.append(word)
    
# print('Words:', lst)
# print('Counting...')
# print('Counts', counts)


# part2
  
# counts = {'chuck' : 1, 'david' : 5, 'cathy' : 7}
# for key in counts:
#   print(key, counts[key])
  
#part3

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
  words = line.split()
  for word in words:
    counts
