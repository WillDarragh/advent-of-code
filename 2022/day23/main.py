# Advent of Code 2022 Day 23

from pprint import pprint

from icecream import ic

def print_map(map):
  for m in map:
    print(''.join(m))

N = (-1, 0)
NE = (-1, 1)
NW = (-1, -1)

S = (1, 0)
SE = (1, 1)
SW = (1, -1)

W = (0, -1)

E = (0, 1)

DIRS = (N, NE, NW, S, SE, SW, E, W)

Ns = (NE, NW, N)
Ss = (SE, SW, S)
Ws = (SW, NW, W)
Es = (SE, NE, E)


with open('input.txt') as f:
  data = f.read()

map = []

elves = []

ROUNDS = 100

for line in data.split('\n'):
  map.append(list(line))

ROWS = len(map)
COLS = len(map[0])

# expand map
map = [['.']*COLS]*ROUNDS + map + [['.']*COLS]*ROUNDS

ROWS = len(map)
for r in range(ROWS):
  map[r] = ['.']*ROUNDS + map[r] + ['.']*ROUNDS

COLS = len(map[0])

for r in range(ROWS):
  for c in range(COLS):
    if map[r][c] == '#':
      elves.append((r, c))

ic.disable()

ic(elves)

first_dir = 0

round = 0
#for round in range(ROUNDS):
while(True):

  round += 1
  
  moves = {}

  if first_dir == 0:
    order = 'NSWE'
  elif first_dir == 1:
    order = 'SWEN'
  elif first_dir == 2:
    order = 'WENS'
  elif first_dir == 3:
    order = 'ENSW'
  
  first_dir = (first_dir+1)%4
  
  # consider moves
  for i, elf in enumerate(elves):

    r, c = elf

    ic(round, i, r, c)
    
    for dir in DIRS:
      dr, dc = dir
      nr, nc = r+dr, c+dc
      if map[nr][nc] == '#':
        break
    else:
      ic('Not moving')
      continue

    for dir in order:

      if dir == 'N':
        for n in Ns:
          dr, dc = n
          nr, nc = r+dr, c+dc
          ic(nr, nc)
          if map[nr][nc] == '#':
            break
        else:
          ic('moving N')
          moves[i] = (nr, nc)
          break
      elif dir == 'S':
        for s in Ss:
          dr, dc = s
          nr, nc = r+dr, c+dc
          if map[nr][nc] == '#':
            break
        else:
          ic('moving S')
          moves[i] = (nr, nc)
          break
      elif dir == 'W':
        for w in Ws:
          dr, dc = w
          nr, nc = r+dr, c+dc
          if map[nr][nc] == '#':
            break
        else:
          ic('moving W')
          moves[i] = (nr, nc)
          break
      elif dir == 'E':
        for e in Es:
          dr, dc = e
          nr, nc = r+dr, c+dc
          if map[nr][nc] == '#':
            break
        else:
          ic('moving E')
          moves[i] = (nr, nc)
          break
          
  # Remove duplicate moves
  move_counts = {}
  for move in moves.values():
    if move not in move_counts:
      move_counts[move] = 1
    else:
      move_counts[move] += 1

  final_moves = {}
  
  for i, move in moves.items():
    if move_counts[move] == 1:
      final_moves[i] = move

  if not final_moves:
    print(round)
    exit()
  
  ic(final_moves)
      
  # Redraw map

  for r, c in elves:
    map[r][c] = '.'

  for i, move in final_moves.items():
    elves[i] = move

  for r, c in elves:
    map[r][c] = '#'

Rs, Cs = [], []
for r, c in elves:
  Rs.append(r)
  Cs.append(c)

minR, maxR = min(Rs), max(Rs)
minC, maxC = min(Cs), max(Cs)

empty = 0

for r in range(minR, maxR+1):
  for c in range(minC, maxC+1):
    if map[r][c] == '.':
      empty += 1

print(empty)