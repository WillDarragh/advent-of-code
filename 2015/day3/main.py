# Advent of code 2015 Day 3

with open('input.txt') as f:
  data = f.read()

part_1 = '''
coords = set([(0, 0)])

pos = [0, 0]

for c in data:

  if c == '<':
    pos[0] -= 1
  elif c == '>':
    pos[0] += 1
  elif c == '^':
    pos[1] += 1
  else:
    pos[1] -= 1

  coords.add(tuple(pos))

print(len(coords))
'''

coords = set([(0, 0)])

pos1 = [0, 0]
pos2 = [0, 0]

for i, c in enumerate(data):

  if i%2 == 0:
    if c == '<':
      pos1[0] -= 1
    elif c == '>':
      pos1[0] += 1
    elif c == '^':
      pos1[1] += 1
    else:
      pos1[1] -= 1
    coords.add(tuple(pos1))
  else:
    if c == '<':
      pos2[0] -= 1
    elif c == '>':
      pos2[0] += 1
    elif c == '^':
      pos2[1] += 1
    else:
      pos2[1] -= 1
    coords.add(tuple(pos2))

print(len(coords))