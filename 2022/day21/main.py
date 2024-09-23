# Advent of Code 2022 Day 21

from sympy import Symbol, solve
from pprint import pprint
from functools import lru_cache

@lru_cache
def is_solved(name):
  return name in solved.keys()

def solve1(name):

  if is_solved(name):

    return solved[name]

  else:

    n1, op, n2 = jobs[name].split()

    v1 = solve1(n1)
    v2 = solve1(n2)

    val = int(eval(f'{v1} {op} {v2}'))

    solved[name] = val

    return val

def solve2(name):

  if is_solved(name):

    return solved[name]
  
  else:

    n1, op, n2 = jobs[name].split()

    v1 = solve2(n1)
    v2 = solve2(n2)

    if type(v1) == str or type(v2) == str:
      val = f'({v1} {op} {v2})'
    else:
      val = int(eval(f'{v1} {op} {v2}'))

    solved[name] = val

    return val

with open('input.txt') as f:
  data = f.read()

jobs = {}
solved = {}

part2 = True

for line in data.split('\n'):

  name, line = line.split(': ')

  if part2 and name == 'humn':
    solved['humn'] = 'humn'
    continue

  if part2 and name == 'root':
    root_n1, _, root_n2 = line.split()
  
  for op in ('*', '+', '-', '/'):
    if op in line:
      jobs[name] = line
      break
  else:
    solved[name] = int(line)

#pprint(solved)
#print()
#pprint(jobs)


humn = Symbol('humn')
solve_string = f'solve({solve2(root_n1)} - {solve2(root_n2)}, humn)'
#print(solve_string)

print(eval(solve_string)[0])
