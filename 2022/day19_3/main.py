# Advent of Code 2022 Day 19

RES = range(4)
COSTS = range(3)
ore, clay, obs, geo = range(4)
RESOURCES = ['ore','clay','obsidian','geode']

def enough_r1_for_r2(r1, r2, robots, resources, t):

  global blueprint

  return resources[r1] + robots[r1]*t >= blueprint[r2][r1]*t

def can_afford(resource, resources):

  global blueprint

  for c in COSTS:
    if blueprint[resource][c] > resources[c]:

      return False

  return True

def is_seen(robots, resources, t):

  global seen

  key = (robots, resources)
  
  if not key in seen.keys():
    seen[key] = t
    return False
  else:
    if seen[key] >= t:
      return True
    else:
      return False

def strictly_better(robs1, res1, robs2, res2):

  for i in RES:
    if robs1[i] < robs2[i] or res1[i] < res2[i]:
      return False

  return True

def solve1(robots, resources, t, n):

  global blueprint, maxes, seen, best
  
  if t == 0:
    return resources[geo]

  if is_seen(robots, resources, t):
    return 0

  if not t in best.keys():
    best[t] = (robots, resources)
  else:
    robs, res = best[t]
    if strictly_better(robs, res, robots, resources):
      return 0
    elif strictly_better(robots, resources, robs, res):
      best[t] = (robots, resources)
  
  print(robots, resources, t)
  
  t -= 1
  
  if can_afford(geo, resources):
    robs = ()
    res = ()

    for r in RES:
      res += (robots[r] + resources[r] - blueprint[geo][r],)
      robs += (robots[r] + (1 if r == geo else 0),)

    return solve1(robs, res, t, n)

  scores = []

  for c in COSTS:
    if can_afford(c, resources):
        
      if (robots[c] < maxes[c]):

        if c == ore:
          if enough_r1_for_r2(ore, ore, robots, resources, t):
            if enough_r1_for_r2(ore, clay, robots, resources, t):
              if enough_r1_for_r2(ore, obs, robots, resources, t):
                if enough_r1_for_r2(ore, geo, robots, resources, t):
                  continue

        elif c == clay:
          if enough_r1_for_r2(clay, obs, robots, resources, t):
            continue
            
        elif c == obs:
          if enough_r1_for_r2(obs, geo, robots, resources, t):
            continue
        
        robs = ()
        res = ()

        for r in RES:
          res += (robots[r] + resources[r] - blueprint[c][r],)
          robs += (robots[r] + (1 if r == c else 0),)
          
        scores.append(solve1(robs, res, t, n))

  robs = ()
  res = ()

  for r in RES:
    res += (robots[r] + resources[r],)
    robs += (robots[r],)
    
  scores.append(solve1(robs, res, t, n))
  
  return max(scores)
    
with open('input.txt') as f:
  data = f.read()

qualities = []

part2 = True

for line in data.split('Blueprint '):

  t = 32 if part2 else 24

  if not line:
    continue

  blueprint = [None, None, None, None]
  
  line = line.strip()

  N, line = line.split(':')
  N = int(N)
  
  line = line.strip()

  for resource in RES:

    _, line = line.split(f'Each {RESOURCES[resource]} robot costs ')
    
    period_index = line.index('.')
    costs, line = line[:period_index], line[period_index+1:]
    line = line.strip()

    costs = costs.split(' and ')

    costs_dict = [0,0,0,0]
    for c in costs:
      n, r = c.split()
      
      costs_dict[['ore','clay','obsidian'].index(r)] = int(n)

    blueprint[resource] = costs_dict

  robots = (1,0,0,0)
  resources = (0,0,0,0)
  
  maxes = [1,1,1]

  for r in RES:
    for c in COSTS:
      if r != c:
        if blueprint[r][c] > maxes[c]:
          maxes[c] = blueprint[r][c]

  print(f'Solving number {N}...')

  seen = {}
  best = {}
  
  geodes = solve1(robots, resources, t, N)
  
  qualities.append(geodes * (1 if part2 else N))

  print(f'Number {N} is {geodes}.')

print('Final Answer:', 0 if part2 else sum(qualities))