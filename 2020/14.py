
from itertools import product
from functools import lru_cache
from more_itertools import locate

def part1(data):

  lines = data.split('\n')

  mem = {}

  mask = 'X'*36

  for line in lines:

    instruction, value = line.split(' = ')

    if instruction == 'mask':

      mask = value

    else:

      loc = instruction[4:-1]

      val = list(f'{bin(int(value))[2:]:0>36}')

      for i in range(36):

        if mask[i] != 'X':

          val[i] = mask[i]

      mem[loc] = ''.join(val)

  values = list(mem.values())

  int_values = [int(v, 2) for v in values]

  return sum(int_values)

@lru_cache
def get_combos(n):

  args = [['0','1'] for i in range(n)]

  return list(product(*args))

def part2(data):

  lines = data.split('\n')

  mem = {}

  mask = 'X'*36

  for line in lines:

    instruction, value = line.split(' = ')

    if instruction == 'mask':

      mask = value

    else:

      loc = instruction[4:-1]

      loc = list(f'{bin(int(loc))[2:]:0>36}')

      val = int(value)

      for i in range(36):

        if mask[i] == '1':

          loc[i] = '1'

      X_count = mask.count('X')

      X_pos = list(locate(mask, lambda x: x == 'X'))

      combos = get_combos(X_count)

      for combo in combos:

        temp_loc = list(loc)

        for X_i in range(X_count):

          pos = X_pos[X_i]

          temp_loc[pos] = combo[X_i]

        int_loc = int(''.join(temp_loc), 2)

        mem[int_loc] = val

  values = list(mem.values())

  return sum(values)
