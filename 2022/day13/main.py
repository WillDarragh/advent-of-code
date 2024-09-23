# Advent of Code 2022 Day 13

from copy import deepcopy
from time import sleep

def sort(L):

  for i in range(len(L)):

    item = deepcopy(L[i])

    smallest = deepcopy(item)
    smallest_i = i
    
    for j in range(i, len(L)):

      if compare(L[j], smallest) == True:
        smallest = deepcopy(L[j])
        smallest_i = j
    
    L[i] = smallest
    L[smallest_i] = item

    

def compare(l, r):

  #print(l,r)
  #sleep(1)
  
  if (type(1) == type(l)) and (type(1) == type(r)):
    if l > r:
      return False
    elif l == r:
      return 'EQ'
    else:
      return True

  elif (type(1) == type(l)):
    right = deepcopy(r)
    left = [l]
    return compare(left, right)
  
  elif type(1) == type(r):
    left = deepcopy(l)
    right = [r]
    return compare(left, right)

  else:
    for i in range(len(l)):
      
      if i >= len(r):
        return False

      if not compare(l[i],r[i]):
        return False
      if compare(l[i], r[i]) == True:
        return True
  
  return True

with open('input.txt') as f:
  data = f.read()

pairs = []

for line in data.split('\n\n'):
  pairs.append(line)

packs = []
for i, pair in enumerate(pairs, 1):
  l,r = pair.split('\n')

  l = eval(l)
  r = eval(r)
  packs.append(l)
  packs.append(r)

packs.append([[6]])
packs.append([[2]])

sort(packs)

mults = []

for i, p in enumerate(packs, 1):
  if p == [[2]] or p ==[[6]]:
    mults.append(i)

print(mults[0]*mults[1])