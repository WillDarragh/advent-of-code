# Advent of Code 2022 Day 24

from math import inf

from copy import copy, deepcopy
from functools import lru_cache

from icecream import ic

DIRS = {'<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)}

UDLR = ((-1, 0), (1, 0), (0, -1), (0, 1))

@lru_cache
def get_blizs(steps):

  global BLIZS
  
  if steps == 0:
    return BLIZS

  blizs = get_blizs(steps-1)

  new_blizs = []

  for rc, d in blizs:

    r, c = rc
    dr, dc = d
    nr, nc = r+dr, c+dc
    
    if nr == 0:
      nr = ROWS-2
    elif nr == ROWS-1:
      nr = 1
    elif nc == 0:
      nc = COLS-2
    elif nc == COLS-1:
      nc = 1
    
    new_blizs.append(((nr, nc), d))

  return tuple(new_blizs)  

def print_map(r, c, bliz_set):

  global ROWS, COLS

  map = [['#']*COLS]

  for row in range(ROWS-2):
    map.append(['#'] + ['.']*(COLS-2) + ['#'])

  map.append(['#']*COLS)

  for br, bc in bliz_set:
    map[br][bc] = '*'

  map[r][c] = 'E'

  for row in map:
    print(''.join(row))
  print()

with open('input.txt') as f:
  data = f.read()

map = []

for line in data.split('\n'):
  map.append(line)

ROWS = len(map)
COLS = len(map[0])

START = 0, 1

GOAL = ROWS-1, COLS-2

blizs = []

for r in range(ROWS):
  for c in range(COLS):
    item = map[r][c]
    if item in DIRS.keys():
      blizs.append(((r, c), DIRS[item]))

STATES = {}

BLIZS = tuple(blizs)

blizs = tuple(blizs)

best = inf

tests = [(0, 1, START)]

while tests:

  tests_copy = copy(tests)
  
  for test in tests_copy:

    steps, phase, rc = test
    
    steps += 1
    
    r, c = rc

    blizs = get_blizs(steps)
  
    bliz_set = set([b[0] for b in blizs])
  
    state = (rc, phase, blizs)
    if not state in STATES:
      STATES[state] = steps
    else:
      if STATES[state] <= steps:
        tests.remove(test)
        continue
      else:
        STATES[state] = steps

    next_phase = False
    
    for d in UDLR:
  
      dr, dc = d
  
      nr, nc = r+dr, c+dc
  
      if (1 <= nr <= ROWS-2) and (1 <= nc <= COLS-2):
  
        pos = nr, nc
  
        if not pos in bliz_set:
          tests.append((steps, phase, (nr, nc)))
  
      elif (phase == 1) and ((nr, nc) == GOAL):
          print('Moving to phase 2 after', steps)
          #tests.append((steps, 2, (nr, nc)))
          tests = [(steps, 2, (nr, nc))]
          next_phase = True
          break
        
      elif (phase == 2) and ((nr, nc) == START):
          print('Moving to phase 3 after', steps)
          #tests.append((steps, 3, (nr, nc)))
          tests = [(steps, 3, (nr, nc))]
          next_phase = True
          break

      elif (phase == 3) and ((nr, nc) == GOAL):
        print('Found solution in', steps)
        if steps < best:
          best = steps

    if next_phase:
      break
    
    if not rc in bliz_set:
      tests.append((steps, phase, rc))

    tests.remove(test)

print(best)