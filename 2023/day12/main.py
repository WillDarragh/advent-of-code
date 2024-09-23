from copy import copy
from pprint import pprint
import re

with open('input.txt', 'r') as f:
  data = f.read()

counts = 0

CHECK = 1

'''
for line in data.split('\n'):
  print(CHECK)
  CHECK += 1
  springs, groups = line.split()
  springs_list = list(springs)
  groups = list(map(int, groups.split(',')))
  G = len(groups)

  unknowns = springs.count('?')
  arrangements = 2**unknowns

  unknowns_i = [m.start() for m in finditer(r'\?', springs)]
  
  for a in range(arrangements):
    bin_a = [int(x) for x in bin(a)[2:].rjust(unknowns, '0')]
    s = copy(springs_list)
    for i, working in zip(unknowns_i, bin_a):
      s[i] = '#' if working else '.'
    
    g = findall(r'\#+', ''.join(s))

    if len(g) == G:
      for m, l in zip(g, groups):
        if len(m) != l:
          break
      else:
        counts += 1
'''

for line in data.split('\n'):
  print(CHECK)
  CHECK += 1
  springs, groups = line.split()
  springs = '?'.join([springs]*5)
  groups = list(map(int, ','.join([groups]*5).split(',')))

  Gs = len(groups)
  SGs = sum(groups)
  Ss = len(springs)
  
  workings = [m.span() for m in re.finditer(r'\#+', springs)]

  possible_groups = {}
  
  for working in workings:

    possible_groups[working] = []

    start, stop = working
    size = stop-start

    before = 0
    after = SGs + Gs - 1
    
    for i, group in enumerate(groups):

      after -= group
      if group >= size:

        if start >= before and stop <= Ss-after:
          possible_groups[working].append((i, group))
          
      before += group + 1
      after -= 1
  
  while (any(len(pgs) == 1 for g, pgs in possible_groups.items())):
    for g, pgs in possible_groups.items():
      if len(pgs) == 1:
        pg = pgs[0]
        # Remove from all others
        for ng, npgs in possible_groups.items():
          if ng != g:
            if pg in npgs:
              npgs.remove(pg)
        start, stop = g
        size = stop-start
        springs = springs[:start] + 'Y'*size + springs[stop:]
        possible_groups.pop(g)
        break

  print(springs)
  pprint(possible_groups)