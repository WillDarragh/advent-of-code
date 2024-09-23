# Advent of Code 2022 Day 17

from copy import deepcopy, copy
from pprint import pprint
from time import sleep

def cprint(chamber, H=0, rock=None):
  c = deepcopy(chamber)

  if rock:
    h = 0
    for r in rock:
      c[H+h] |= r
      h += 1
  
  print()
  for row in c[::-1]:
    print('|',end='')
    bin_str = bin(row)[2:]
    bin_str = bin_str.rjust(7, '0')
    for b in bin_str:
      if b == '1':
        print('#',end='')
      else:
        print('.',end='')
    print('|',end='')
    print()
  print('+'+'-'*7+'+')
  print()   

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
    rock_row = '00'
    for c in row:
      if c == '@':
        rock_row += '1'
      else:
        rock_row += '0'
    rock_row += '0'*(7-len(row)-2)
    rock.append(int(rock_row, 2))
  rocks.append(rock)

rocks_mod = len(rocks)

heights = [len(r) for r in rocks]

ROCKS = 1000000000000
#ROCKS = 2022
#ROCKS = 30000

chamber = []

print('Done with setup...')
print()

j = 0

H = 0

part1 = 0

for R in range(ROCKS):

  if not part1:
    break

  rmod = R%rocks_mod

  rock = copy(rocks[rmod])
  height = heights[rmod]
  
  for r in range(3+height):
    chamber.append(0)
  
  settled = False

  i = 0

  H += 3

  #cprint(chamber, H, rock)
  
  while True:

    # Jet move
    if i%2 == 0:

      jet = jets[j%j_mod]
      j += 1

      # Right
      if jet == '>':
        can_move = True
        for h in range(height):
          row_i = H + h
          row = chamber[row_i]
          r = rock[h]

          if bin(r|row).count('1') != bin((r>>1)|row).count('1'):
            can_move = False
            break
            
        if can_move:
          for h in range(height):
            rock[h] >>= 1
          
      # Left
      else:
        can_move = True
        for h in range(height):
          row_i = H + h
          row = chamber[row_i]
          r = rock[h]

          if bin(r|row).count('1') != bin((r<<1)|row).count('1'):
            can_move = False
            break

          if r<<1 > 127:
            can_move = False
            break
            
        if can_move:
          for h in range(height):
            rock[h] <<= 1

    # Fall
    else:

      # Check
      for h in range(height):
        row_i = H + h
        row = chamber[row_i]
        r = rock[h]
        new_row_i = row_i - 1
        new_row = chamber[new_row_i]

        if new_row_i < 0:
          settled = True
          break

        if bin(r|new_row).count('1') != (bin(r).count('1') + bin(new_row).count('1')):
          settled = True
          break

      if settled:       
        break

      # down

      H -= 1

    #cprint(chamber, H, rock)
      
    # end settling
    i += 1

  for h in range(height):
    row_i = H + h
    r = rock[h]

    chamber[row_i] |= r
  
  i = -1
  
  while True:
    if chamber[i] == 0:
      i -= 1
    else:
      break

  H = len(chamber) + i + 1

  chamber = chamber[:H]

  #print(f'{R+1} done')
  #cprint(chamber)

if part1:
  print('Part 1 height is...')
  print(len(chamber))
  print()

################
# Part 2
################

chamber = []

j = 0
H = 0
R = 0

print('Do until height 8000 to find pattern...')
print()

while H < 8000:
  
  rmod = R%rocks_mod

  rock = copy(rocks[rmod])
  height = heights[rmod]
  
  for r in range(3+height):
    chamber.append(0)
  
  settled = False

  i = 0

  H += 3

  #cprint(chamber, H, rock)
  
  while True:

    # Jet move
    if i%2 == 0:

      jet = jets[j%j_mod]
      j += 1

      # Right
      if jet == '>':
        can_move = True
        for h in range(height):
          row_i = H + h
          row = chamber[row_i]
          r = rock[h]

          if bin(r|row).count('1') != bin((r>>1)|row).count('1'):
            can_move = False
            break
            
        if can_move:
          for h in range(height):
            rock[h] >>= 1
          
      # Left
      else:
        can_move = True
        for h in range(height):
          row_i = H + h
          row = chamber[row_i]
          r = rock[h]

          if bin(r|row).count('1') != bin((r<<1)|row).count('1'):
            can_move = False
            break

          if r<<1 > 127:
            can_move = False
            break
            
        if can_move:
          for h in range(height):
            rock[h] <<= 1

    # Fall
    else:

      # Check
      for h in range(height):
        row_i = H + h
        row = chamber[row_i]
        r = rock[h]
        new_row_i = row_i - 1
        new_row = chamber[new_row_i]

        if new_row_i < 0:
          settled = True
          break

        if bin(r|new_row).count('1') != (bin(r).count('1') + bin(new_row).count('1')):
          settled = True
          break

      if settled:       
        break

      # down

      H -= 1

    #cprint(chamber, H, rock)
      
    # end settling
    i += 1

  for h in range(height):
    row_i = H + h
    r = rock[h]

    chamber[row_i] |= r
  
  i = -1
  
  while True:
    if chamber[i] == 0:
      i -= 1
    else:
      break

  H = len(chamber) + i + 1

  chamber = chamber[:H]

  R += 1

print('Searching for patterns...')
print()

found = None

for size in range(2671, 2672):
#for size in range(len(chamber)//2, 1, -1):
  if found:
    break
  for start in range(2418, 2419):
  #for start in range(len(chamber)//2):
    if found:
      break
    old = chamber[start:start+size]
    for i in range(start, len(chamber)//2, size):
      new = chamber[i:i+size]
      if old != new:
        break
    else:
      found = start, size

print('Pattern found...')
print(found)
print()

print('Finding number of rocks in pattern...')
print()

h_before, h_pattern = found
h_total = h_before + h_pattern

chamber = []

j = 0
H = 0
R = 0
count = 0
before = 0

while H < h_total:
  
  if H >= h_before:
    count += 1
  else:
    before += 1
  
  rmod = R%rocks_mod

  rock = copy(rocks[rmod])
  height = heights[rmod]
  
  for r in range(3+height):
    chamber.append(0)
  
  settled = False

  i = 0

  H += 3

  #cprint(chamber, H, rock)
  
  while True:

    # Jet move
    if i%2 == 0:

      jet = jets[j%j_mod]
      j += 1

      # Right
      if jet == '>':
        can_move = True
        for h in range(height):
          row_i = H + h
          row = chamber[row_i]
          r = rock[h]

          if bin(r|row).count('1') != bin((r>>1)|row).count('1'):
            can_move = False
            break
            
        if can_move:
          for h in range(height):
            rock[h] >>= 1
          
      # Left
      else:
        can_move = True
        for h in range(height):
          row_i = H + h
          row = chamber[row_i]
          r = rock[h]

          if bin(r|row).count('1') != bin((r<<1)|row).count('1'):
            can_move = False
            break

          if r<<1 > 127:
            can_move = False
            break
            
        if can_move:
          for h in range(height):
            rock[h] <<= 1

    # Fall
    else:

      # Check
      for h in range(height):
        row_i = H + h
        row = chamber[row_i]
        r = rock[h]
        new_row_i = row_i - 1
        new_row = chamber[new_row_i]

        if new_row_i < 0:
          settled = True
          break

        if bin(r|new_row).count('1') != (bin(r).count('1') + bin(new_row).count('1')):
          settled = True
          break

      if settled:       
        break

      # down

      H -= 1

    #cprint(chamber, H, rock)
      
    # end settling
    i += 1

  for h in range(height):
    row_i = H + h
    r = rock[h]

    chamber[row_i] |= r
  
  i = -1
  
  while True:
    if chamber[i] == 0:
      i -= 1
    else:
      break

  H = len(chamber) + i + 1

  chamber = chamber[:H]

  R += 1

rock_num = R
j_num = j

solution = 0

rocks_left = ROCKS

rocks_left -= before
solution += h_before

patterns = rocks_left // count

rocks_left -= count*patterns
solution += h_pattern*patterns

print('After patterns and starts, rocks left and curr height...')
print(rocks_left, solution)
print()

print('Doing last pattern and extra rocks...')
print()

H = h_total-h_before
chamber = chamber[h_before:h_total]

j = j_num

for R in range(rocks_left):

  rmod = (rock_num+R)%rocks_mod

  rock = copy(rocks[rmod])
  height = heights[rmod]
  
  for r in range(3+height):
    chamber.append(0)
  
  settled = False

  i = 0

  H += 3

  #cprint(chamber, H, rock)
  
  while True:

    # Jet move
    if i%2 == 0:

      jet = jets[j%j_mod]
      j += 1

      # Right
      if jet == '>':
        can_move = True
        for h in range(height):
          row_i = H + h
          row = chamber[row_i]
          r = rock[h]

          if bin(r|row).count('1') != bin((r>>1)|row).count('1'):
            can_move = False
            break
            
        if can_move:
          for h in range(height):
            rock[h] >>= 1
          
      # Left
      else:
        can_move = True
        for h in range(height):
          row_i = H + h
          row = chamber[row_i]
          r = rock[h]

          if bin(r|row).count('1') != bin((r<<1)|row).count('1'):
            can_move = False
            break

          if r<<1 > 127:
            can_move = False
            break
            
        if can_move:
          for h in range(height):
            rock[h] <<= 1

    # Fall
    else:

      # Check
      for h in range(height):
        row_i = H + h
        row = chamber[row_i]
        r = rock[h]
        new_row_i = row_i - 1
        new_row = chamber[new_row_i]

        if new_row_i < 0:
          settled = True
          break

        if bin(r|new_row).count('1') != (bin(r).count('1') + bin(new_row).count('1')):
          settled = True
          break

      if settled:       
        break

      # down

      H -= 1

    #cprint(chamber, H, rock)
      
    # end settling
    i += 1

  for h in range(height):
    row_i = H + h
    r = rock[h]

    chamber[row_i] |= r
  
  i = -1
  
  while True:
    if chamber[i] == 0:
      i -= 1
    else:
      break

  H = len(chamber) + i + 1

  chamber = chamber[:H]

extra = H - h_pattern

print('Extra rocks addded...')
print(extra)
print()

print('Final solution...')
print(solution+extra)
print() 

#print(1523, 1695) # rocks start, pat
#print(2418, 2671) # pat start, len

