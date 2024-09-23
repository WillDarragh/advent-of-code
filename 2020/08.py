
def part1(data):

  lines = data.split('\n')

  coms = []

  for i, line in enumerate(lines):

    a, b = line.split()

    coms.append([a, int(b)])

  for i,com in enumerate(coms):

    acc = 0

    visited = []

    curr = 0

    newcoms = []

    the_com = None

    if com[0] == 'jmp':

      newcoms = list(coms)
      newcoms[i] = ['nop', com[1]]

      the_com = com

    elif com[0] == 'nop':

      newcoms = list(coms)
      newcoms[i] = ['jmp', com[1]]

      the_com = com

    else:

      newcoms = list(coms)

    while curr not in visited and curr < len(coms):

      visited.append(curr)

      #print(curr, len(newcoms))

      com, i = newcoms[curr]

      if com=='acc':

        acc += i

        curr += 1

      elif com=='jmp':

        curr += i

      else:

        curr += 1

    #print(curr, len(coms), the_com)

    if curr >= len(coms):

      return acc
  

def part2(data):

  pass
