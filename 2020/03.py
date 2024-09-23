
def part1(data):
    __import__('time').sleep(1)
    # Data is automatically read from 01.txt
    return "".join(reversed(data))

def part2(data):
  data = data.split('\n')

  slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]

  all_trees = 1

  for dr,dc in slopes:

    trees = 0

    r, c = 0, 0

    while r < len(data)-1:

      r += dr
      c += dc

      if data[r][c%len(data[0])] == '#':

        trees += 1

    all_trees *= trees

  return all_trees

'''
def part2(data):
  data = data.split('\n')
'''
