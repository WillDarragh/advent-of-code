# Advent of Code 2022 Day 22

# Right, Down, Left, Up
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

# Down
def next_r(r, c):
  global map, ROWS

  newr = r
  
  if newr == ROWS-1:
    newr = 0
  else:
    newr += 1

  while (map[newr][c] == ' '):
    if newr == ROWS-1:
      newr = 0
    else:
      newr += 1

  return newr, map[newr][c]

# Up
def prev_r(r, c):
  global map, ROWS

  newr = r
  
  if newr == 0:
    newr = ROWS-1
  else:
    newr -= 1

  while (map[newr][c] == ' '):
    if newr == 0:
      newr = ROWS-1
    else:
      newr -= 1

  return newr, map[newr][c]

# Right
def next_c(r, c):
  global map, COLS
  
  newc = c
  
  if newc == COLS-1:
    newc = 0
  else:
    newc += 1

  while (map[r][newc] == ' '):
    if newc == COLS-1:
      newc = 0
    else:
      newc += 1

  return newc, map[r][newc]

def prev_c(r, c):
  global map, COLS

  newc = c
  
  if newc == 0:
    newc = COLS-1
  else:
    newc -= 1

  while (map[r][newc] == ' '):
    if newc == 0:
      newc = COLS-1
    else:
      newc -= 1

  return newc, map[r][newc]

with open('input.txt') as f:
  data = f.read()

data_map, data_path = data.split('\n\n')

map = data_map.split('\n')

lengths = [len(m) for m in map]

max_length = max(lengths)

for i in range(len(map)):

  length = len(map[i])
  dif = max_length - length
  map[i] = map[i] + ' '*dif

ROWS = len(map)
COLS = len(map[0])

Di = 0

r, c = 0, 0

while (map[r][c] != '.'):

  c += 1

path = []

num = ''
for char in data_path:
  if char in 'RL':
    path.append(num)
    path.append(char)
    num = ''
  else:
    num += char
path.append(num)

path = [p for p in path if p]

for move in path:
  
  if move == 'R':

    Di = (Di+1)%4

  elif move == 'L':

    Di = (Di-1)%4

  else:

    num = int(move)
    
    if Di == 0:
      for n in range(num):
        newc, val = next_c(r, c)
        if val != '#':
          c = newc
        else:
          break
    elif Di == 1:
      for n in range(num):
        newr, val = next_r(r, c)
        if val != '#':
          r = newr
        else:
          break
    elif Di == 2:
      for n in range(num):
        newc, val = prev_c(r, c)
        if val != '#':
          c = newc
        else:
          break
    elif Di == 3:
      for n in range(num):
        newr, val = prev_r(r, c)
        if val != '#':
          r = newr
        else:
          break

print(1000 * (r+1) + 4 * (c+1) + Di)