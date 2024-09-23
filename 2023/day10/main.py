
class Pipe:
  global R, C
  r: int
  c: int
  symbol: str
  lefts: list
  rignts: list

  def __init__(self, r, c, symbol):
    self.r = r
    self.c = c
    self.symbol = symbol

S = 'S'
J = 'J'
F = 'F'
L = 'L'
l = '|'
h = '-'
s = '7'

pipes = [S, J, F, L, l, h, s]

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

dirs = [UP, DOWN, LEFT, RIGHT]

MOVES = {
  (RIGHT, h): RIGHT,
  (LEFT, h): LEFT,
  (RIGHT, J): UP,
  (DOWN, J): LEFT,
  (UP, F): RIGHT,
  (LEFT, F): DOWN,
  (DOWN, L): RIGHT,
  (LEFT, L): UP,
  (UP, l): UP,
  (DOWN, l): DOWN,
  (RIGHT, s): DOWN,
  (UP, s): LEFT
}

with open('input.txt', 'r') as f:
  data = f.read()


matrix = []

for line in data.split('\n'):
  matrix.append(list(line))

R = len(matrix)
C = len(matrix[0])

start = []

for ri, row in enumerate(matrix):
  for ci, item in enumerate(row):
    if item == S:
      start = (ri, ci)

curr = start
next = (-1,-1)
move = (0,0)

for dr, dc in dirs:
  cr, cc = curr
  nr, nc = cr+dr, cc+dc
  if (0<=nr<R) and (0<=nc<C):
    item = matrix[nr][nc]
    if item in pipes:
      next =  (nr, nc)
      move = (dr, dc)
      if (move, item) in MOVES:
        break

'''
moves = 1

while (matrix[next[0]][next[1]] != S):
  curr = next
  cr, cc = curr
  item = matrix[cr][cc]
  move = MOVES[(move, item)]
  dr, dc = move
  next = (cr+dr, cc+dc)
  moves += 1
  
print(moves/2)
'''

