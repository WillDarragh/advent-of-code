
from copy import deepcopy
from itertools import product

ds = [[-1,0,1] for i in range(3)]
all_dirs = list(product(*ds))
all_dirs.remove((0,0,0))

ds2 = [[-1,0,1] for i in range(4)]
all_dirs2 = list(product(*ds2))
all_dirs2.remove((0,0,0,0))

def my_print(space):

  for X in space:

    for Y in X:

      print(''.join(Y))

    print()

def part1(data):

  flat = data.split('\n')

  N = len(flat)+13

  space = [[['.' for i in range(N)] for j in range(N)] for k in range(N)]

  for i in range(len(flat)):
    for j in range(len(flat[0])):
      space[0][i][j] = flat[i][j]

  #my_print(space)

  for cycle in range(6):

    print('Cycle', cycle)

    new_space = deepcopy(space)

    for z in range(N):
      for i in range(N):
        for j in range(N):
          neighbors = 0
          for dz, di, dj in all_dirs:
            nz, ni, nj = z+dz, i+di, j+dj
            nz, ni, nj = nz%N, ni%N, nj%N
            if space[nz][ni][nj] == '#':
              neighbors += 1
          if space[z][i][j] == '#':
            if neighbors == 2 or neighbors == 3:
              pass
            else:
              new_space[z][i][j] = '.'
          else:
            if neighbors == 3:
              new_space[z][i][j] = '#'

    space = deepcopy(new_space)

    #my_print(space)

  active = 0

  for Z in space:
    for i in Z:
      active += i.count('#')

  return active

def part2(data):

  flat = data.split('\n')

  N = len(flat)+13

  space = [[[['.' for i in range(N)] for j in range(N)] for k in range(N)] for l in range(N)]

  for i in range(len(flat)):
    for j in range(len(flat[0])):
      space[0][0][i][j] = flat[i][j]

  #my_print(space)

  for cycle in range(6):

    print('Cycle', cycle)

    new_space = deepcopy(space)

    for z in range(N):
      for i in range(N):
        for j in range(N):
          for k in range(N):
            neighbors = 0
            for dz, di, dj, dk in all_dirs2:
              nz, ni, nj, nk = z+dz, i+di, j+dj, k+dk
              nz, ni, nj, nk = nz%N, ni%N, nj%N, nk%N
              if space[nz][ni][nj][nk] == '#':
                neighbors += 1
            if space[z][i][j][k] == '#':
              if neighbors == 2 or neighbors == 3:
                pass
              else:
                new_space[z][i][j][k] = '.'
            else:
              if neighbors == 3:
                new_space[z][i][j][k] = '#'

    space = deepcopy(new_space)

    #my_print(space)

  active = 0

  for Z in space:
    for i in Z:
      for j in i:
        active += j.count('#')

  return active