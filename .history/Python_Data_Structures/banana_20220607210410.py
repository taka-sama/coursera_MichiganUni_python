number = 'X-DSPAM-Confidence:    0.8475'
atpos = number.find('0')
print(atpos) #0 → 23

sppos = number.find('5')
print(sppos) #5 → 28

onlynum = number[atpos : sppos+1]
print(onlynum)
