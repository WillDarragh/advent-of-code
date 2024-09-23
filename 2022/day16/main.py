# Advent of Code 2022 Day 16

from copy import copy, deepcopy
from pprint import pprint
from math import inf

def solve(curr, time, score, unvisited):

  global graph, rates

  unvisited.remove(curr)

  scores = []
  
  for name in unvisited:

    dist = graph[curr][name]
    
    tent_time = time - dist - 1

    value = rates[name] * tent_time

    if tent_time >= 0:
      scores.append(solve(name, tent_time, value, copy(unvisited)))

  if scores:
    score += max(scores)
    
  return score

with open('input.txt') as f:
  data = f.read()
  
rates = {}
graph = {}
names = []

for line in data.split('\n'):

  _, trimmed = line.split('Valve ')

  name, trimmed = trimmed.split(' has flow rate=')

  if 'tunnels' in trimmed:
    rate, trimmed = trimmed.split('; tunnels lead to valves ')
  else:
    rate, trimmed = trimmed.split('; tunnel leads to valve ')

  rate = int(rate)
  
  tunnels = trimmed.split(', ')

  names.append(name)
  graph[name] = tunnels
  rates[name] = rate
  
shortests = {name: {} for name in names}

for start, tunnels in graph.items():

  unvisited = copy(names)
    
  tentative = {name: inf for name in names}

  tentative[start] = 0

  curr = start
  
  while unvisited:

    new_distance = tentative[curr] + 1
    
    for next in graph[curr]:
      
      if new_distance < tentative[next]:

        tentative[next] = new_distance

    unvisited.remove(curr)

    next_best = inf
    
    for un in unvisited:
      if tentative[un] < next_best:
        next_best = tentative[un]
        curr = un
    
  shortests[start] = tentative

print('Calculated shortest distances...')
print()

names = [n for n in names if rates[n]]

graph = {'AA': {n: shortests['AA'][n] for n in names}}

for name in names:
  graph[name] = {n: shortests[name][n] for n in names if name != n}

print('Created reduced graph...')
print()

#part1 = '''
curr = 'AA'
time = 30
score = 0
unvisited = copy(names) + ['AA']

print(solve(curr, time, score, unvisited))
print()
#'''

N = len(unvisited)

best = 0

print(f'Checking {2**N} combinations...')

for n in range(2**N):

  print(n)
  
  s = bin(n)[2:]
  s = s.ljust(N, '0')

  uns1 = ['AA']
  uns2 = ['AA']

  for i, bit in enumerate(s):
    if bit == '1':
      uns1.append(unvisited[i])
    else:
      uns2.append(unvisited[i])


  s1 = solve('AA', 26, 0, uns1)
  s2 = solve('AA', 26, 0, uns2)

  S = s1+s2

  if S > best:

    best = S

print(best)