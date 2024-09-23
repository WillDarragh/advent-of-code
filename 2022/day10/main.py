# Advent of Code 2022 Day 10

def draw(v):
  spirte = ['.' for i in range(40)]

  spirte[v] = '#'
  if v-1 >= 0:
    spirte[v-1] = '#'
  if v+1 < 40:
    spirte[v+1] = '#'

  return(spirte)
  
with open('input.txt') as f:
  data = f.read()

lines = data.split('\n')

cycle = 1

line_num = 0

X = 1

reg = None

sum = 0

screen_i = 0
screen = [[] for i in range(6)]

sprite = '###' + '.'*37

while (line_num < len(lines)) or reg:

  if cycle < 25:
    print(cycle)
    print(sprite)
  
  if screen_i < 6:
    screen[screen_i].append(sprite[(cycle-1)%40])
  
  if cycle in list(range(0,260,40)):
    #print(X)
    screen_i += 1
    sum += cycle*X
  
  if line_num < len(lines):
    line = lines[line_num]
  else:
    line = ''

  if reg:
    X += reg
    reg = None
    cycle += 1
    sprite = draw(X)

  else:
    if line.startswith('noop'):
      pass
    else:
      _, v = line.split()
      reg = int(v)

    cycle += 1
    line_num += 1

  #print(cycle, X)

print(sum)

print(len(screen[0]))
for r in screen:
  for c in r:
    print(c, end='')
  print()