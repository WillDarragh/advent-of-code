

def part1(data):

  nums = list(map(int, data.split('\n')))
  i = 25

  for n in range(i, len(nums)):

    num = nums[n]

    #print(f'num {num}')

    for x in range(n-i, n):

      for y in range(n-i, n):

        #print(nums[x], nums[y])
        if nums[x] + nums[y] == num:

          #print(f'found for {num} {(nums[x], nums[y])}')

          break

      else:

        continue

      break

    else:

      break

  return num
  


def part2(data):

  nums = list(map(int, data.split('\n')))
  
  N = 217430975

  for x in range(len(nums)):

    for y in range(len(nums)):

      if sum(nums[x:y]) == N:

        ran = nums[x:y]

        return min(ran) + max(ran)