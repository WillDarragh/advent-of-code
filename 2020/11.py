
from pprint import pprint
from copy import deepcopy

def part1(data):

  return

  curr = data.split('\n')

  curr = [list(r) for r in curr]

  R, C = len(curr), len(curr[0])

  last = []

  adj = [[0, 1],
         [1, 0],
         [-1,0],
         [0,-1],
         [1, 1],
         [-1,1],
         [1,-1],
         [-1,-1]]

  while (curr != last):

    new = deepcopy(curr)

    for r in range(R):

      for c in range(C):

        occ = 0

        for dr, dc in adj:

          newr, newc = r + dr, c + dc

          if not (0 <= newr and newr < R):
            continue
          if not (0 <= newc and newc < C):
            continue


          if curr[newr][newc] == '#':
            occ += 1


        if curr[r][c] == 'L' and occ == 0:
          new[r][c] = '#'

        if curr[r][c] == '#' and occ >= 4:
          new[r][c] = 'L'

    #pprint(curr)

    #pprint(new)

    last = deepcopy(curr)

    curr = deepcopy(new)

  count = 0

  for row in curr:
    count += row.count('#')

  return count


        

def part2(data):

  curr = data.split('\n')

  curr = [list(r) for r in curr]

  R, C = len(curr), len(curr[0])

  last = []

  adj = [[0, 1],
         [1, 0],
         [-1,0],
         [0,-1],
         [1, 1],
         [-1,1],
         [1,-1],
         [-1,-1]]

  while (curr != last):

   # pprint(curr)
    #print()

    new = deepcopy(curr)

    for r in range(R):

      for c in range(C):

        occ = 0

        for dr, dc in adj:

          newr, newc = r, c

          while(1):

            newr, newc = newr + dr, newc + dc

            if not (0 <= newr and newr < R):
              break
            if not (0 <= newc and newc < C):
              break

            if curr[newr][newc] == '#':
              #print(f'{r}, {c} found occ at {newr}, {newc}')
              occ += 1
              break
            elif curr[newr][newc] == 'L':
              break


        if curr[r][c] == 'L' and occ == 0:
          new[r][c] = '#'

        if curr[r][c] == '#' and occ >= 5:
          new[r][c] = 'L'

    #pprint(curr)

    #pprint(new)

    last = deepcopy(curr)

    curr = deepcopy(new)

  count = 0

  for row in curr:
    count += row.count('#')

  return count
