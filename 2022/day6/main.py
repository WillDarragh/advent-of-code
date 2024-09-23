# Advent of Code 2022 Day 6

with open('input.txt') as f:
  data = f.read()

last_14 = ['0' for i in range(14)]

i = 1

for c in data:

  last_14.pop()

  last_14.insert(0, c)
  
  if i >= 14 and (sorted(list(set(last_14))) == sorted(last_14)):

    break

  i += 1

print(i)