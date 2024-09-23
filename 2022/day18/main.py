# Advent of Code 2022 Day 18

X, Y, Z = 0, 1, 2

def adj(p1, p2):

  difs = []
  
  for i in range(3):
    difs.append(abs(p1[i]-p2[i]))
  
  if difs.count(1) == 1 and difs.count(0) == 2:
    return True

  return False

def num_adj(p1):

  global points

  count = 0
  
  for p2 in points:

    if adj(p1, p2):
      count += 1

      if count == 6:
        break

  return count

def flood(curr, p_set):

  global points, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax, known_external

  x, y, z = curr
  
  if curr in points:
    return True

  if curr in known_external:
    return False
  
  if not (Xmin <= x <= Xmax):
    return False

  if not (Ymin <= y <= Ymax):
    return False

  if not (Zmin <= z <= Zmax):
    return False

  p_set.add(curr)

  dirs = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]

  for d in dirs:
    dx, dy, dz = d

    new = (x+dx, y+dy, z+dz)

    if not new in p_set:
      if not flood(new, p_set):
        return False

  return True

with open('input.txt') as f:
  data = f.read()


Xs = []
Ys = []
Zs = []

points = []

for line in data.split('\n'):
  x, y, z = map(int, line.split(','))

  points.append((x,y,z))

  Xs.append(x)
  Ys.append(y)
  Zs.append(z)

sides = 0

for pi in range(len(points)):

  s = 6
  
  p1 = points[pi]

  for pj in range(len(points)):
    
    p2 = points[pj]
  
    if p1 == p2:
      continue
    
    if adj(p1, p2):
      s -= 1

    if s == 0:
      break

  sides += s

print(sides)

Xmin, Xmax = min(Xs), max(Xs)
Ymin, Ymax = min(Ys), max(Ys)
Zmin, Zmax = min(Zs), max(Zs)

pockets = 0

known_pockets = set()
known_external = set()

for x in range(Xmin, Xmax+1):
  for y in range(Ymin, Ymax+1):
    for z in range(Zmin, Zmax+1):
      p = (x,y,z)

      p_set = set()
      
      if not p in points:

        if not p in known_external:

          if not p in known_pockets:
            if flood(p, p_set):
              
              known_pockets |= p_set
    
            else:
    
              known_external |= p_set

internal_sides = 0

for p in known_pockets:
  internal_sides += num_adj(p)

print(sides - internal_sides)