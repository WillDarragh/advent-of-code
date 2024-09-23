
from numpy import lcm

def part1(data):

  data = data.split('\n')

  depart = int(data[0])

  buses = list(map(int, [d for d in data[1].split(',') if d != 'x']))

  fastest = 99999999999
  busid = -1

  for i, bus in enumerate(buses):

    curr = buses[i]

    while(curr < depart):

      curr += bus

    if curr < fastest:

      fastest = curr
      busid = bus

  return (fastest-depart)*busid


def part2(data):

  data = data.split('\n')

  buses = [b if b == 'x' else int(b) for b in data[1].split(',')]

  len_all = len(buses)

  diffs = []

  index = 0

  while (index < len_all - 1):

    diff = index+1

    while (buses[index+1] == 'x'):

      index += 1
      diff += 1

    index += 1

    diffs.append(diff)

  buses = [b for b in buses if b != 'x']

  inc = buses[0]

  goal = buses[0]

  len_buses = len(buses)

  for i in range(len_buses-1):
    next_val = buses[i+1]
    next_off = diffs[i]

    while((goal+next_off) % next_val):
      goal += inc
    inc*=next_val

  return goal