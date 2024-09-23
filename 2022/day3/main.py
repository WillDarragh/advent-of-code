# Advent of Code 2022 Day 3

from string import ascii_letters as als

with open('input.txt') as f:
  data = f.read()

sack = []

total = 0

for i, line in enumerate(data.split()):

  if i%3 == 0:
    sack = [line]
  elif (i-1)%3 == 0:
    sack.append(line)
  else:
    sack.append(line)
  
    #mid = len(line)//2
  
    #a = line[:mid]
  
    #b = line[mid:]
  
    for c in als:
      if c in sack[0]:
        if c in sack[1]:
          if c in sack[2]:
            total += als.index(c) + 1

print(total)