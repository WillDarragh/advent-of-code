
def part1(data):

  data = data.split('\n')

  data = [[d[0], int(d[1:])] for d in data]

  r, c = 0, 0

  facing_index = 0

  facing = [[0, 1], [-1, 0], [0, -1], [1, 0]]

  for d, i in data:

    if d == 'F':

      dr, dc = [f*i for f in facing[facing_index%4]]

      r += dr
      c += dc

    elif d == 'N':

      r += i

    elif d == 'S':

      r -= i

    elif d == 'E':

      c += i

    elif d == 'W':

      c -= i

    elif d == 'R':
      facing_index += i//90
    elif d == 'L':
      facing_index -= i//90

  return abs(r) + abs(c)

def part2(data):

  data = data.split('\n')

  data = [[d[0], int(d[1:])] for d in data]

  wr, wc = 1, 10

  r, c = 0, 0

  for d, i in data:

    if d == 'F':

      r += wr*i
      c += wc*i

    elif d == 'N':

      wr += i

    elif d == 'S':

      wr -= i

    elif d == 'E':

      wc += i

    elif d == 'W':

      wc -= i

    elif d == 'R':
    
      for t in range(i//90):

        wr, wc = wc*-1, wr

    elif d == 'L':
      for t in range(i//90):

        wr, wc = wc, wr*-1

    print(d, i, r, c, wr, wc)

  return abs(r) + abs(c)
