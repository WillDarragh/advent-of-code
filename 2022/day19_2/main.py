# Advent of Code 2022 Day 19

from pprint import pprint
from copy import deepcopy
from math import comb

T = 24

RES = ('ore', 'clay', 'obsidian', 'geode')
ore, clay, obs, geo = RES

def can_afford(resource, resources):

  for r, c in blueprint[resource].items():

    if c > resources[r]:

      return False

  return True

def solve1(robots, resources, t):

  global blueprint, maxes
  
  if t == 0:
    return resources[geo]

  t -= 1

  #print('-'*(T-t), t)

  if can_afford(geo, resources):
    #print('time', T-t)
    robs = deepcopy(robots)
    res = deepcopy(resources)

    for re, n in robs.items():
      res[re] += n
    
    robs[geo] += 1
    for r, c in blueprint[geo].items():
      res[r] -= c

    return solve1(robs, res, t)

  scores = []

  for r in (ore, clay, obs):
    if can_afford(r, resources):

      if (resources[r] <= maxes[r]):
        
        robs = deepcopy(robots)
        res = deepcopy(resources)

        for re, n in robs.items():
          res[re] += n
        
        robs[r] += 1
        for k, v in blueprint[r].items():
          res[k] -= v

        scores.append(solve1(robs, res, t))

  robs = deepcopy(robots)
  res = deepcopy(resources)

  for re, n in robs.items():
    res[re] += n
  scores.append(solve1(robs, res, t))

  return max(scores)
    

with open('input.txt') as f:
  data = f.read()

blueprints = []

qualities = 0

for line in data.split('Blueprint '):

  t = 24

  if not line:
    continue

  blueprint = {}
  
  line = line.strip()

  N, line = line.split(':')
  N = int(N)
  
  line = line.strip()

  robots = {}
  resources = {}
  
  for resource in RES:

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

  robots[ore] = 1
  
  maxes = {r: 1 for r in (ore, clay, obs)}

  for robot, costs in blueprint.items():
    for r, c in costs.items():
      if r != geo:
        if c > maxes[r]:
          maxes[r] = c

  print(f'Solving number {N}')

  geodes = solve1(robots, resources, T)

  print(geodes)
  qualities += geodes * N

  print(f'Finished number {N} with quality {geodes*N}\n')

print(qualities)