# Advent of Code 2022 Day 1

with open('input.txt') as f:
  txt = f.read()

top_3 = [0, 0, 0]

for set in txt.split('\n\n'):

  top_3.sort()
  
  total = 0
  for thing in set.split('\n'):
    if thing:
      total += int(thing)

  if total > top_3[0]:
    top_3[0] = total

print(sum(top_3))