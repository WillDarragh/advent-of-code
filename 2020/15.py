
from pprint import pprint

def part1(data):

  nums = list(map(int, data.split(',')))

  spoken = []

  spoken_before = set()

  n = 1

  last_num = nums[0]

  for num in nums:

    spoken_before.add(last_num)

    spoken.insert(0, num)

    last_num = num

    n += 1

  while (n <= 2020):

    new_num = 0

    if last_num not in spoken_before:

      spoken_before.add(last_num)

    else:

      new_num = spoken.index(last_num, 1)

    spoken.insert(0, new_num)

    last_num = new_num

    n += 1

  return last_num

def part2(data):

  nums = list(map(int, data.split(',')))

  BEFORE = 0
  POS = 1

  D = {}

  n = 1

  num_set = set()

  last_num = None

  for num in nums:

    D[num] = [False, n]

    num_set.add(num)

    if last_num != None:
      D[last_num][BEFORE] = True

    last_num = num

    n += 1

  while (n <= 30000000):

    new_num = 0

    if last_num in num_set:

      if D[last_num][BEFORE]:

        new_num = n - D[last_num][POS] - 1

      D[last_num][POS] = n-1

    else:

      num_set.add(last_num)
      D[last_num] = [False, n-1]

    D[last_num][BEFORE] = True

    last_num = new_num

    n += 1

  return last_num