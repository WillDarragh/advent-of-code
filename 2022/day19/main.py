# Advent of Code 2022 Day 19

from pprint import pprint
from copy import deepcopy
from itertools import product

RES = ('clay', 'geode', 'obsidian', 'ore')

T = 24

def can_affords(plan, resources):

  global blueprint
  
  res = deepcopy(resources)

  for r, n in plan.items():
    
    if can_afford(r, resources) >= n:

      costs = blueprint[r]

      for k, v in costs.items():

        res[k] -= n*v

    else:

      return False

  return True

def can_afford(resource, resources):

  global blueprint

  costs = blueprint[resource]

  ns = [resources[r]//c for r,c in costs.items()]
  
  return min(ns)

def stupid(robots, resources, t):

  global blueprint
  
  if t == 0:
    return resources['geode']
  
  for k, v in robots.items():
    resources[k] += v

  t -= 1
  
  scores = []

  for r in RES:
    if can_afford(r, resources):

      robs = deepcopy(robots)
      res = deepcopy(resources)

      robs[r] += 1

      costs = bluepinrt[r]

      for k, v in costs.items():
        res[k] -= blueprint[k]
        
      scores.append(solve1(robs, res, t))

  robs = deepcopy(robots)
  res = deepcopy(resources)

  scores.append(solve1(robs, res, t))

  return max(scores)

def smart(robots, resouces, t):

  global blueprint
  
  if t == 0:
    return resources['geode']
  
  for k, v in robots.items():
    resources[k] += v

  t -= 1
  
  scores = []

  for r in RES:
    if can_afford(r, resources):

      robs = deepcopy(robots)
      res = deepcopy(resources)

      robs[r] += 1

      costs = bluepinrt[r]

      for k, v in costs.items():
        res[k] -= blueprint[k]
        
      scores.append(solve1(robs, res, t))

  robs = deepcopy(robots)
  res = deepcopy(resources)

  scores.append(solve1(robs, res, t))

  return max(scores)

def solve1(robots, resources, t):

  global blueprint
  
  if t == 0:
    return resources['geode']
  
  for k, v in robots.items():
    resources[k] += v

  t -= 1
  
  #print(f'Minute {T-t}, with resources')
  #pprint(resources)
  #print('with robots')
  #pprint(robots)
  #print()
  
  scores = []

  affords = {}

  for r in RES:
    if can_afford(r, resources) >= 1:
      affords[r] = range(1, can_afford(r, resources)+1)

  keys = list(affords.keys())
  values = list(affords.values())

  if values:
    for costs in product(*values):
      plan = {keys[i]: costs[i] for i in range(len(keys))}
      
      if can_affords(plan, resources):
  
        #pprint(plan)
        
        robs = deepcopy(robots)
        res = deepcopy(resources)
        
        for r, n in plan.items():
  
          robs[r] += n
  
          costs = blueprint[r]
  
          for k, v in costs.items():
  
            res[k] -= v*n
  
          #print(f'Buying {n} {r} robots')
  
       # print()
        
        scores.append(solve1(robs, res, t))

  robs = deepcopy(robots)
  res = deepcopy(resources)

  scores.append(solve1(robs, res, t))

  return max(scores)

with open('input.txt') as f:
  data = f.read()

blueprints = []

for line in data.split('Blueprint '):

  if not line:
    continue

  blueprint = {}
  
  line = line.strip()

  N, line = line.split(':')
  
  line = line.strip()

  robots = {}
  resources = {}
  
  for resource in ('ore', 'clay', 'obsidian', 'geode'):

    _, line = line.split(f'Each {resource} robot costs ')

    period_index = line.index('.')
    costs, line = line[:period_index], line[period_index+1:]
    line = line.strip()

    costs = costs.split(' and ')

    costs_dict = {}
    for c in costs:
      n, r = c.split()
      costs_dict[r] = int(n)

    blueprint[resource] = costs_dict

    robots[resource] = 0

    resources[resource] = 0

  robots['ore'] = 1
  
  geodes = stupid(robots, resources, T)

  print(geodes)
  
  break