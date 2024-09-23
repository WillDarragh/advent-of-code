# Advent of Code 2022 Day 17

from copy import deepcopy
from pprint import pprint

with open('input.txt') as f:
  data = f.read()

jets = data
j_mod = len(data)

rocks = []
r1 = ['@@@@']
r2 = ['.@.', '@@@', '.@.']
r3 = ['@@@', '..@', '..@']
r4 = ['@', '@', '@', '@']
r5 = ['@@', '@@']

for r in [r1, r2, r3, r4, r5]:
  rock = []
  for row in r:
    rock_row = ['.']*2

    for c in row:
      rock_row.append(c)

    rock_row += ['.']*(7-len(row)-2)
    rock.append(rock_row)
  rocks.append(rock)

rocks_mod = len(rocks)

heights = [len(r) for r in rocks]

ROCKS = 1000000000000
ROCKS = 2022

cmin = 0
cmax = 6

H = 0

chamber = []

j = 0

for R in range(ROCKS):

  rmod = R%rocks_mod

  rock = deepcopy(rocks[rmod])
  height = heights[rmod]
  
  for r in range(3):
    chamber.append(['.' for c in range(7)])

  H += 3

  chamber += rock

  rmin = H
  rmax = H+height-1
  
  #pprint(chamber[::-1])
  #print()
  
  settled = False

  i = 0
  
  while True:

    # Jet move
    if i%2 == 0:

      jet = jets[j%j_mod]
      j += 1

      # Right
      if jet == '>':
        can_move = True
        for r in range(rmin, rmax+1):
          for c in range(cmax, cmin-1, -1):
            if chamber[r][c] == '@':
              newc = c+1
              if newc > cmax or chamber[r][newc] != '.':
                can_move = False
                break
              else:
                break      
        if can_move:
          for r in range(rmin, rmax+1):
            for c in range(cmax, cmin-1, -1):
              if chamber[r][c] == '@':
                newc = c+1
                chamber[r][newc] = '@'
                chamber[r][c] = '.'
      # Left
      else:
        can_move = True
        for r in range(rmin, rmax+1):
          for c in range(cmin, cmax+1):
            if chamber[r][c] == '@':
              newc = c-1
              if newc < 0 or chamber[r][newc] != '.':
                can_move = False
                break
              else:
                break      
        if can_move:
          for r in range(rmin, rmax+1):
            for c in range(cmin, cmax+1):
              if chamber[r][c] == '@':
                newc = c-1
                chamber[r][newc] = '@'
                chamber[r][c] = '.'

    # Fall
    else:
      for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
          if chamber[r][c] == '@':
            newr = r-1
            if newr < 0 or chamber[newr][c] not in '.@':
              settled = True
              break

      if settled:
        for r in range(rmin, rmax+1):
          for c in range(cmin, cmax+1):
            if chamber[r][c] == '@':
              chamber[r][c] = '#'
              
        break

      # down
      for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
          if chamber[r][c] == '@':
            newr= r-1
            chamber[newr][c] = '@'
            chamber[r][c] = '.'

      rmin -= 1
      rmax -= 1

    #pprint(chamber[::-1])
    #print()
    
    # end settling
    i += 1

  i = -1
  
  while True:
    if '#' in chamber[i]:
      break
    i -= 1

  H = len(chamber) + i + 1

  chamber = chamber[:H]

print(len(chamber))

comment = '''
print()
for r in chamber[::-1]:
  print('|',end='')
  print(''.join(r),end='')
  print('|',end='')
  print()
print('-'*9)
'''