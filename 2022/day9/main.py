# Advent of Code 2022 Day 9

with open('input.txt') as f:
  data = f.read()

r = 0
c= 1

changes = {'R': [0,1], 'L': [0,-1], 'U': [1,0], 'D': [-1,0]}

Hr, Hc = 0, 0

TS = [[0,0] for i in range(9)]

Ts = set()

for line in data.split('\n'):

  d, n = line.split()

  n = int(n)

  dr, dc = changes[d]

  for i in range(n):

    Hr += dr
    Hc += dc
    
    for t in range(9):

      if t == 0:
        HTr = Hr - TS[t][r]
        HTc = Hc - TS[t][c]

      else:
        HTr = TS[t-1][r] - TS[t][r]
        HTc = TS[t-1][c] - TS[t][c]
      
      # exact one away
      if ((abs(HTr) == 1) != (abs(HTc) == 1)) and ((HTr == 0) != (HTc == 0)):
        pass
        
      # one away each
      elif (abs(HTr) == 1) and (abs(HTc) == 1):
        pass
        
      # two away horiz
      elif (HTr == 0):
        TS[t][c] += HTc/2
        
      # two away vert
      elif (HTc == 0):
        TS[t][r] += HTr/2
        
      # diagonal away 1 horiz
      else:
        TS[t][r] += HTr/abs(HTr)
        TS[t][c] += HTc/abs(HTc)

      if t == 8:
        Ts.add((int(TS[t][r]), int(TS[t][c])))

print(len(Ts))

part_1 = '''

Tr, Tc, Hr, Hc = 0, 0, 0, 0

changes = {'R': [0,1], 'L': [0,-1], 'U': [1,0], 'D': [-1,0]}

Ts = set()

for line in data.split('\n'):

  d, n = line.split()

  n = int(n)

  dr, dc = changes[d]

  for i in range(n):

    Hr += dr
    Hc += dc

    HTr = Hr-Tr
    HTc = Hc-Tc

    print(f'{line} step {i} H: {Hr},{Hc} - T: {Tr},{Tc}')
    
    # exact one away
    if ((abs(HTr) == 1) != (abs(HTc) == 1)) and ((HTr == 0) != (HTc == 0)):
      print('exact one away')
    # one away each
    elif (abs(HTr) == 1) and (abs(HTc) == 1):
      print('one one diag')
    # two away horiz
    elif (HTr == 0):
      print('just horiz')
      Tc += HTc/2
    # two away vert
    elif (HTc == 0):
      print('just vert')
      Tr += HTr/2
    # diagonal away 1 horiz
    else:
      print('diag')
      Tr += HTr/abs(HTr)
      Tc += HTc/abs(HTc)
      
    Ts.add((int(Tr), int(Tc)))

  print('Head',Hr,Hc)
  print('Tail',Tr,Tc)
  print()

print(len(Ts))
'''