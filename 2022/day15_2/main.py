# Advent of Code 2022 Day 15

def fill_man(rc, dist):

  global mat, ROWS, COLS, minx, miny, Yoff, Xoff, THEY

  R, C = rc
  
  for d in range(1,dist+1):

    for i in range(d+1):

      r = i
      c = d-i

      for mod in [(1,1), (-1,1), (1,-1), (-1,-1)]:

        modr, modc = mod

        newr = R+r*modr
        newc = C+c*modc

        if newr >= ROWS:
          ROWS += 1
          mat.append(['.' for c in range(COLS)])
        if newr < 0:
          ROWS += 1
          mat.insert(0, ['.' for c in range(COLS)])
          miny -= 1
          Yoff -= 1
          THEY += 1
          R += 1
          newr = 0
        if newc >= COLS:
          COLS += 1
          for row in mat:
            row.append('.')
        if newc < 0:
          COLS += 1
          for row in mat:
            row.insert(0, '.')
          minx -= 1
          Xoff -= 1
          C += 1
          newc = 0
        if mat[newr][newc] == '.':
          mat[newr][newc] = '#'

def mans(val, dist):

  maxval = dist*2 + 1

  return (maxval - val*2)

def get_nopes(rc, dist):

  global mat, ROWS, COLS, minx, miny, Yoff, Xoff, THEY, NOPES

  R, C = rc

  delta_r = abs(THEY - R)

  if delta_r <= dist:

    NOPES.add(C)

    for i in range(dist - delta_r):

      NOPES.add(C+(i+1))
      NOPES.add(C-(i+1))

def man_dist(a, b):

  ar, ac = a
  br, bc = b

  dr = abs(ar - br)
  dc = abs(ac - bc)

  return (dr+dc)

def conv(xy):

  global minx, miny

  x, y = xy
  
  r = y - miny
  c = x - minx
  
  return (r, c)

def get_xy(s):

  x, y = s.split(', ')

  x = int(x[2:])
  y = int(y[2:])

  return (x, y)

def reduce(ranges, r):

  a1, b1 = r
  
  for rani in range(len(ranges)):
    
    ran = ranges[rani]
    
    a2, b2 = ran
    
    # completely inside
    if a1 >= a2 and b1 <= b2:
      return

    # completely covers
    if a1 < a2 and b1 > b2:
      ranges.pop(rani)
      reduce(ranges, r)
      return

    # left overlap
    if a1 < a2 and b1 >= a2 - 1:
      ranges.pop(rani)
      newrange = (a1, b2)
      reduce(ranges, newrange)
      return

    # right overlap
    if b1 > b2 and a1 <= b2 + 1:
      ranges.pop(rani)
      newrange = (a2, b1)
      reduce(ranges, newrange)
      return

  ranges.append(r)

def solve(rc, dist):

  global Rs, Cs, RMAX, CMAX, RMIN, CMIN, Yoff, Xoff

  R, C = rc

  minr = R - dist
  minc = C - dist
  
  for i in range(2*dist+1):

    r = minr + i

    dif = abs(dist-i)
    
    if r < RMIN:
      continue
    if r > RMAX:
      break

    mincol = C-(dist-dif)
    maxcol = C+(dist-dif)

    if mincol < CMIN:
      mincol = CMIN
    if maxcol > CMAX:
      maxcol = CMAX

    ri = r+Yoff
    
    reduce(Rs[ri], (mincol,maxcol))

  for i in range(2*dist+1):

    c = minc + i

    dif = abs(dist-i)
    
    if c < CMIN:
      continue
    if c > CMAX:
      break

    minrow = R-(dist-dif)
    maxrow = R+(dist-dif)

    if minrow < RMIN:
      minrow = RMIN
    if maxrow > RMAX:
      maxrow = RMAX

    ci = c+Xoff
      
    reduce(Cs[ci], (minrow,maxrow))

    
with open('input.txt') as f:
  data = f.read()

Xs = []
Ys = []

for line in data.split('\n'):

  if not line:
    break
    
  _, trimmed = line.split('Sensor at ')

  S, B = trimmed.split(': closest beacon is at ')

  Sx, Sy = get_xy(S)
  Bx, By = get_xy(B)

  Xs += [Sx, Bx]
  Ys += [Sy, By]

minx = min(Xs)
maxx = max(Xs)
miny = min(Ys)
maxy = max(Ys)
Xoff = minx
Yoff = miny

ROWS = maxy - miny + 1
COLS = maxx - minx + 1

mat = None
#mat = [['.' for c in range(COLS)] for r in range(ROWS)]

coords = list(zip(Xs, Ys))

pairs = [[coords[i], coords[i+1]] for i in range(0,len(coords),2)]

THEMAX = 4000000

THEY = THEMAX
THEY -= Yoff

THEX = THEMAX
THEX -= Xoff

RMIN = 0 - Yoff
RMAX = THEY
CMIN = 0 - Xoff
CMAX = THEX 

Rs = [[] for r in range(THEMAX+1)]
Cs = [[] for r in range(THEMAX+1)]

for pair in pairs:
  
  S, B = pair
  
  Src = conv(S)
  Brc = conv(B)

  Sr, Sc = Src
  Br, Bc = Brc
  
  #mat[Sr][Sc] = 'S'
  #mat[Br][Bc] = 'B'

  dist = man_dist(Src, Brc)

  #fill_man(Src, dist)
  #get_nopes(Src, dist)
  solve(Src, dist)

  print('calculating...')

for i, r in enumerate(Rs):
  if len(r) != 1:
    Y = i

for i, c in enumerate(Cs):
  if len(c) != 1:
    X = i

print(4000000*X + Y)
