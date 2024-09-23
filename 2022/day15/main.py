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

def solve(rc, dist):

  global RNOPES, CNOPES, RMAX, CMAX, RMIN, CMIN, Yoff, Xoff

  R, C = rc

  for row in range(RMIN, RMAX):

    delta_r = abs(row-R)
    
    if delta_r <= dist:

      r = row+Yoff

      max_delta = dist-delta_r
      
      lower = C - max_delta
      higher = C + max_delta

      if lower <= CMAX and higher >= CMIN:

        if lower < CMIN:
          lower = CMIN
        if higher > CMAX:
          higher = CMAX
          
      RNOPES[r].append((lower,higher))
      #reduce(RNOPES[r])


  for col in range(CMIN, CMAX):

    delta_c = abs(col-C)
    
    if delta_c <= dist:

      c = col+Xoff
      
      max_delta = dist-delta_c
      
      lower = R - max_delta
      higher = R + max_delta

      if lower <= RMAX and higher >= RMIN:

        if lower < RMIN:
          lower = RMIN
        if higher > RMAX:
          higher = RMAX
          
      CNOPES[c].append((lower,higher))
      #reduce(CNOPES[c])

def reduce(ranges):
  
  for a in range(len(ranges)):
    for b in range(len(ranges)):
      if a != b:
        x1, y1 = ranges[a]
        x2, y2 = ranges[b]
        if x1 >= x2 and y1 <= y2:
          ranges.pop(a)
          reduce(ranges)
          return
        elif x1 <= x2 and y1 >= y2:
          ranges.pop(b)
          reduce(ranges)
          return
        elif x1 < x2:
          if y1 >= x2-1:
            new = (x1, y2)
            ranges.pop(a)
            ranges.pop(b-1)
            ranges.append(new)
            reduce(ranges)
            return
    
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

RNOPES = [[] for r in range(THEMAX)]
CNOPES = [[] for r in range(THEMAX)]

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

for i, r in enumerate(RNOPES):
  if len(r) != 1:
    Y = i

for i, c in enumerate(CNOPES):
  if len(c) != 1:
    X = i

print(4000000*X + Y)
