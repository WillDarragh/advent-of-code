# Advent of Code 2022 Day 

VALS = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}

def to_dec(snafu): 

  I = len(snafu)-1
  i = len(snafu)-1
  
  dec = 0

  while (i >= 0):

    d = snafu[i]
    
    mult = 5**(I-i)
    
    if d == '=':
      dec += -2*mult
    elif d == '-':
      dec += -1*mult
    elif d == '0':
      dec += 0*mult
    elif d == '1':
      dec += 1*mult
    elif d == '2':
      dec += 2*mult
    
    i -= 1

  return dec

def to_snafu(dec):

  I = 0

  copy = dec

  while (copy > 1):

    copy = copy / 5
    I += 1

  snafu = ''
  
  for i in range(I-1, -1, -1):
    mult = 5**i

    dif = sum([2*(5**j) for j in range(i)])

    count = 0
    
    if dec > 0:
      while (dec - mult) >= -1*dif:
        count += 1
        dec -= mult
    elif dec < 0:
      while (dec + mult) <= dif:
        count -= 1
        dec += mult
      
    snafu += VALS[count]   

  return snafu

with open('input.txt') as f:
  data = f.read()

total = 0

for line in data.split('\n'):

  total += to_dec(line)

print(total)
print(to_snafu(total))