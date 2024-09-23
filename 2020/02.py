def part1(data):
    __import__('time').sleep(1)
    # Data is automatically read from 01.txt
    return "".join(reversed(data))

'''
def part2(data):

  badlines = data.split()

  count = 0

  lines = []

  for n in range(0, len(badlines), 3):

    lines.append(badlines[n:n+3])

  print(len(lines))

  for line in lines:

    rule, char, pw = line

    low, high = rule.split('-')

    char = char[:-1]

    if int(low) <= pw.count(char) <= int(high):

      count += 1

  return count

'''
def part2(data):

  badlines = data.split()

  count = 0

  lines = []

  for n in range(0, len(badlines), 3):

    lines.append(badlines[n:n+3])

  for line in lines:

    rule, char, pw = line

    low, high = map(int, rule.split('-'))

    char = char[:-1]

    if int(pw[low-1]==char) + int(pw[high-1]==char) == 1:

      count += 1

  return count
