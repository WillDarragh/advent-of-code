# Advent of Code 2022 Day 14

def fall(r, c):

  global mat, ROWS, COLS, minX, minY, floor

  test = '''
  for row in range(ROWS):
    for col in range(COLS):
      if (row,col) == (r,c):
        print('*',end='')
      else:
        print(mat[row][col],end='')
    print()
  print()
  '''
  
  if r+1 >= ROWS:
    mat[r][c] = 'o'
    return True

  if mat[r+1][c] == '.':
    return fall(r+1, c)

  if c-1 < 0:
    for row in mat:
      row.insert(0, '.')
    COLS += 1
    minX -= 1
    return fall(r+1, 0)

  if mat[r+1][c-1] == '.':
    return fall(r+1, c-1)

  if c+1 >= COLS:
    for row in mat:
      row.append('.')
    COLS += 1
    return fall(r+1, c+1)

  if mat[r+1][c+1] == '.':
    return fall(r+1, c+1)

  if (r,c) == conv([500, 0]):
    return False
    
  mat[r][c] = 'o'
  return True

def conv(coord):

  global ROWS, COLS, minX, minY

  x, y = list(map(int, coord))
  
  r = y

  c = x - minX

  return((r, c))

with open('input.txt') as f:
  data = f.read()

Xs = []
Ys = []

for line in data.split('\n'):
  
  for coords in line.split(' -> '):

    x,y = coords.split(',')

    Xs.append(int(x))
    Ys.append(int(y))

Xs.append(500)
Ys.append(0)

minX = min(Xs)
minY = min(Ys)
maxX = max(Xs)
maxY = max(Ys)

ROWS = maxY - minY + 1 + 1
COLS = maxX - minX + 1

floor = ROWS + 1

mat = [['.' for j in range(COLS)] for i in range(ROWS)]

for line in data.split('\n'):

  coords = [coord.split(',') for coord in line.split(' -> ')]
  
  start = conv(coords.pop())

  while(coords):
    
    stop = conv(coords.pop())

    r1, c1 = start
    r2, c2 = stop
    
    if r1 == r2:

      delta = int((c2 - c1)/abs(c2 - c1))

      if delta == 1:
        while(c1 <= c2):
          mat[r1][c1] = '#'
          c1 += 1
      else:
        while(c1 >= c2):
          mat[r1][c1] = '#'
          c1 -= 1
    
    elif c1 == c2:

      delta = int((r2 - r1)/abs(r2 - r1))

      if delta == 1:
        while(r1 <= r2):
          mat[r1][c1] = '#'
          r1 += 1
      else:
        while(r1 >= r2):
          mat[r1][c1] = '#'
          r1 -= 1

    start = stop

units = 0

r, c = conv([500,0])

mat[r][c] = '+'

while(fall(r, c)):
  units += 1
  r, c = conv([500,0])

print(units+1)