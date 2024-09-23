# Advent of Code 2022 Day 22

# Right, Down, Left, Up
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
R, D, L, U = range(4)

def region(r, c):

  global N, ROWS, COLS
  
  if 0 <= c < N:
    return 2

  if N <= c < 2*N: 
    return 3

  if 3*N <= c < COLS:
    return 6

  else:

    if 0 <= r < N:
      return 1

    if N <= r < 2*N:
      return 4

    if 2*N <= r < ROWS:
      return 5

# Down
def next_r(r, c):
  global map, ROWS, COLS, Di, N

  newr = r

  reg = region(r, c)

  if reg == 3:
    if r == 2*N - 1:
      r_off = c - N
      newr = 3*N - r_off - 1
      newc = 2*N
      return newr, newc, map[newr][newc], R
      
  elif reg == 2:
    if r == 2*N - 1:
      newr = 3*N - 1
      c_off = c
      newc = 3*N - c_off - 1
      return newr, newc, map[newr][newc], U
      
  elif reg == 5:
    if r == 3*N - 1:
      newr = 2*N - 1
      c_off = c - 2*N
      newc = N - c_off - 1
      return newr, newc, map[newr][newc], U
    
  elif reg == 6:
    if r == 3*N - 1:
      newc = 0
      r_off = c - 3*N
      newr = 2*N - r_off - 1
      return newr, newc, map[newr][newc], R

  newr += 1
  return newr, c, map[newr][c], D

# Up
def prev_r(r, c):
  global map, ROWS, COLS, Di, N

  newr = r

  reg = region(r, c)
  
  if reg == 1:
    if r == 0:
      newr = N
      c_off = c - 2*N
      newc = N - c_off - 1
      return newr, newc, map[newr][newc], D

  elif reg == 2:
    if r == N:
      newr = 0
      c_off = c
      newc = 3*N - c_off - 1
      return newr, newc, map[newr][newc], D

  elif reg == 3:
    if r == N:
      newc = 2*N
      r_off = c - N
      newr = r_off
      return newr, newc, map[newr][newc], R

  elif reg == 6:
    if r == 2*N:
      newc = 3*N - 1
      r_off = c - 3*N
      newr = 2*N - r_off - 1
      return newr, newc, map[newr][newc], L

  newr -= 1
  return newr, c, map[newr][c], U

# Right
def next_c(r, c):
  global map, COLS, ROWS, Di, N
  
  newc = c
  
  reg = region(r, c)

  if reg == 1:
    if c == 3*N - 1:
      newc = 4*N - 1
      r_off = r
      newr = 3*N - r_off - 1
      return newr, newc, map[newr][newc], L
      
  elif reg == 4:
    if c == 3*N -1:
      newr = 2*N
      c_off = r - N
      newc = 4*N - c_off - 1
      return newr, newc, map[newr][newc], D
    
  elif reg == 6:
    if c == 4*N - 1:
      newc = 3*N - 1
      r_off = r - 2*N
      newr = N - r_off - 1
      return newr, newc, map[newr][newc], L
      
  
  newc += 1
  return r, newc, map[r][newc], R

# Left
def prev_c(r, c):
  global map, COLS, ROWS, Di, N

  newc = c

  reg = region(r, c)

  if reg == 1:
    if c == 2*N:
      newr = N
      c_off = r
      newc = N + c_off
      return newr, newc, map[newr][newc], D
    
  elif reg == 2:
    if c == 0:
      newr = 3*N - 1
      c_off = r - N
      newc = 4*N - c_off - 1
      return newr, newc, map[newr][newc], U
    
  elif reg == 5:
    if c == 2*N:
      newr = 2*N - 1
      c_off = r - 2*N
      newc = 2*N - c_off - 1
      return newr, newc, map[newr][newc], U
  
  newc -= 1
  return r, newc, map[r][newc], L

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

N = int(len(map)/4)

# Remove 2
to2 = []
for col in range(0, N):
  s = ''
  for row in range(4*N-1, 3*N-1, -1):
    s += map[row][col]
  to2.append(s)
map = map[:3*N]

# Remove 3
to3 = []
for col in range(0, N):
  s = ''
  for row in range(3*N-1, 2*N-1, -1):
    s += map[row][col]
  to3.append(s)
for row in range(len(map)):
  map[row] = map[row][N:]

# Remove 6
to6 = []
for row in range(N-1, 0-1, -1):
  s = ''
  for col in range(2*N-1, N-1, -1):
    s += map[row][col]
  to6.append(s)
for row in range(len(map)):
  map[row] = map[row][:N]

# Reattach
for row in range(len(map)):
  if N <= row < 2*N:
    map[row] = to2[row-N] + to3[row-N] + map[row]
  else:
    map[row] = ' '*2*N + map[row]

for row in range(len(map)):
  if 2*N <= row < 3*N:
    map[row] = map[row] + to6[row-2*N]
  else:
    map[row] = map[row] + ' '*N

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

last_i = len(path)-1

for i, move in enumerate(path):

  if move == 'R':

    Di = (Di+1)%4

  elif move == 'L':

    Di = (Di-1)%4

  else:

    num = int(move)
    
    for n in range(num):
      
      if Di == 0:
        newr, newc, val, di = next_c(r, c)
        if val != '#':
          r, c, Di = newr, newc, di
        else:
          break
      elif Di == 1:
        newr, newc, val, di = next_r(r, c)
        if val != '#':
          r, c, Di = newr, newc, di
        else:
          break
      elif Di == 2:
        newr, newc, val, di = prev_c(r, c)
        if val != '#':
          r, c, Di = newr, newc, di
        else:
          break
      elif Di == 3:
        newr, newc, val, di = prev_r(r, c)
        if val != '#':
          r, c, Di = newr, newc, di
        else:
          break


print(1000 * (r+1) + 4 * (c+1) + Di)

# 79122, 150569, 108676

# 144361