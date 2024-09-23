
def part1(data):

  data = data.split('\n\n')

  count = 0

  for d in data:

    s = set(d)

    s -= {' ', '\n'}

    count += len(s)

  return count

def part2(data):

  data = data.split('\n\n')

  sets = []

  count = 0

  for d in data:

    sets.append(d.split())

  for s in sets:

    all_qs = set()

    for line in s:

      all_qs |= set(line)

    for q in list(all_qs):

      for line in s:

        if q not in line:

          break

      else:

        count += 1

  return count
