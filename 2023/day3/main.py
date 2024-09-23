from pprint import pprint

NUMS = '0123456789'
SYMS = '!@#$%^&*():;<>,?-_+={[}]|\'"\\/'

def valid(r, c):
  global grid, R, C

  tests = [[r+1, c], [r-1, c], [r, c+1], [r, c-1], [r+1, c+1], [r+1, c-1], [r-1, c+1], [r-1, c-1]]

  for test in tests:
    nr, nc = test
    if nr >= 0 and nc >= 0 and nr < R and nc < C:
      x = grid[nr][nc]
      if x != '.' and x not in NUMS:
        return True

  return False

def gear(r, c):
  global grid, R, C

  tests = [[r+1, c], [r-1, c], [r, c+1], [r, c-1], [r+1, c+1], [r+1, c-1], [r-1, c+1], [r-1, c-1]]

  for test in tests:
    nr, nc = test
    if nr >= 0 and nc >= 0 and nr < R and nc < C:
      x = grid[nr][nc]
      if x == '*':
        return (nr, nc)

  return None

with open('input.txt', 'r') as f:
  lines = f.read().split('\n')

grid = [list(line) for line in lines]

R = len(grid)
C = len(grid[0])
'''
nums = []

for r in range(R):

  curr = ''
  processing = False
  val = False
  
  c = 0

  while (c < C):

    x = grid[r][c]

    if x in NUMS:

      curr += x

      processing = True

      if not val:
        val = valid(r, c)

    else:

      if processing:

        #print(curr, val, end=' ')
        
        processing = False
        if val:
          nums.append(int(curr))
          #print(curr, end=' ')

        
        val = False
        curr = ''
        
    c += 1

  if processing:
    processing = False
    if val:
      nums.append(int(curr))
    val = False
    curr = ''


print(sum(nums))
'''

gear_parts = {}
good_gears = []

for r in range(R):

  curr = ''
  processing = False
  g = None

  c = 0

  while (c < C):

    x = grid[r][c]

    if x in NUMS:

      curr += x

      processing = True

      if not g:
        g = gear(r, c)

    else:

      if processing:

        #print(curr, val, end=' ')

        processing = False
        if g:
          if g in gear_parts:
            gear_parts[g] *= int(curr)
            good_gears.append(g)
          else:
            gear_parts[g] = int(curr)
          #print(curr, end=' ')


        g = None
        curr = ''

    c += 1

  if processing:
    processing = False
    if g:
      if g in gear_parts:
        gear_parts[g] *= int(curr)
        good_gears.append(g)
      else:
        gear_parts[g] = int(curr)
    g = None
    curr = ''

#print(good_gears)
#print(gear_parts)

total = 0

for g in good_gears:
  total += gear_parts[g]

print(total)