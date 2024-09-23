from functools import lru_cache

def part1(data):

  return

  data = list(map(int, data.split('\n')))

  data.sort()

  data.append(data[-1]+3)

  ones = 0
  twos = 0
  threes = 0

  curr = 0

  for d in data:

    diff = d - curr

    if diff == 1:

      ones += 1

    elif diff == 3:

      threes += 1

    curr = d

  return ones * threes


#############################################

nums = []

@lru_cache(maxsize=256)
def in_nums(n):
  global nums

  return n in nums

@lru_cache(maxsize=256)
def num_pos(n):
  global nums

  return nums.index(n)

def part2(data):

  global nums

  nums = list(map(int, data.split('\n')))

  nums.sort()

  nums.append(nums[-1]+3)

  nums = [0] + nums

  paths = 0

  num_counts = []

  for i, n in enumerate(nums):
    
    if not num_counts:
      num_counts.append(1)

    else:
      
      count = 0

      for m in range(n-3,n):
          if in_nums(m):
            count += num_counts[num_pos(m)]

      num_counts.append(count)
            
  print(nums)
  print(num_counts)

  return num_counts[-1]
