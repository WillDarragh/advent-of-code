# Advent of Code 2022 Day 12

def search(cur, n):

  global mat, shortest, end, bests
  
  n += 1
  
  r, c = cur

  if shortest:

    if n >= shortest:

      return

  if cur in bests.keys():
    if n < bests[cur]:
      bests[cur] = n
    else:
      return
  else:
    bests[cur] = n

  if cur == end:

    #print('found one way')
    
    if not shortest:

      shortest = n
    
    if n < shortest:

      shortest = n

    return
  
  for move in [(0,1), (1,0), (0,-1), (-1,0)]:
    
    new = (r+move[0], c+move[1])

    if new[0] < 0 or new[0] >= len(mat):
      continue

    if new[1] < 0 or new[1] >= len(mat[0]):
      continue

    cur_el = mat[r][c]
    new_el = mat[new[0]][new[1]]
    if ord(new_el) - ord(cur_el) <= 1:
      search(new, n)

bests = {}

with open('input.txt') as f:
  data = f.read()

shortest = None

mat = []

starts = []

for line in data.split('\n'):

  mat.append(list(line))

for row in range(len(mat)):

  for col in range(len(mat[0])):

    if mat[row][col] == 'S':
    
      starts.append((row, col))
      start = (row, col)
    
    if mat[row][col] == 'a':

      starts.append((row, col))

    if mat[row][col] == 'E':

      end = (row, col)

mat[end[0]][end[1]] = 'z'
mat[start[0]][start[1]] = 'a'

for s in starts:
  search(s, 0)

print(shortest)