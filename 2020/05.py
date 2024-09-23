
def part1(data):
  data = data.split('\n')

  ID = 0

  for d in data:

    R = 64

    C = 4

    r0, r1 = 0, 127
    c0, c1 = 0, 7

    for c in d[:7]:

      if c == 'F':
        r1 -= R
      else:
        r0 += R

      R /= 2

    for c in d[7:]:

      if c == 'L':
        c1 -= C
      else:
        c0 += C 
      
      C /= 2

    r = min(r0,r1)
    c = max(c0, c1)

    i = r*8 + c0

    if i > ID:
      ID = i

  return ID

def part2(data):
  data = data.split('\n')

  IDs = []

  for d in data:

      R = 64

      C = 4

      r0, r1 = 0, 127
      c0, c1 = 0, 7

      for c in d[:7]:

        if c == 'F':
          r1 -= R
        else:
          r0 += R

        R /= 2

      for c in d[7:]:

        if c == 'L':
          c1 -= C
        else:
          c0 += C 
        
        C /= 2

      r = min(r0,r1)
      c = max(c0, c1)

      i = r*8 + c0

      IDs.append(int(i))

  IDs.sort()
  
  print(IDs)

  allids = range(min(IDs),max(IDs)+1)

  myid = set(allids) - set(IDs)

  return myid
