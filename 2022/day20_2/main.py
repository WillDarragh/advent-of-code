# Advent of Code 2022 Day 20

from pprint import pprint

with open('input.txt') as f:
  data = f.read()

original = []

curr = []

key = 811589153

part2 = True

id = 0
for line in data.split('\n'):
  n = int(line) * (key if part2 else 1)
  original.append((id, n))
  curr.append((id, n))

  id += 1

mod = len(original)-1

print('Mixing...')
print()

for i in range(10 if part2 else 1):
  for id, n in original:
  
    num = (id, n)
  
    if n == 0:
      continue
    
    index = curr.index(num)
    new = (index + n)%mod
  
    curr.remove(num)
  
    curr.insert(new, num)
  
print('Solving...')
print()

zero_i = None

for i, num in enumerate(curr):

  if num[1] == 0:
    zero_i = i
    break

S = 0

for coord in (1000, 2000, 3000):
  index = (zero_i+coord)%(mod+1)
  S += curr[index][1]

print(S)
