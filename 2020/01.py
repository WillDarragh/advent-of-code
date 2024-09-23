

def part1(data):
    __import__('time').sleep(1)
    return "".join(reversed(data))

def part2(data):

  nums = list(map(int, data.split()))

  ent1, ent2, ent3 = 0, 0, 0 

  for i in range(len(nums)):

    for j in range(i, len(nums)):

      for k in range(j, len(nums)):

        if sum([nums[i], nums[j], nums[k]]) == 2020:

          break

      else:
       
        continue

      break

    else:

      continue

    ent1, ent2, ent3 = nums[i], nums[j], nums[k]

    break

  return ent1*ent2*ent3
