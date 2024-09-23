

'''
with open('input.txt', 'r') as f:
  lines = f.read().split('\n')

sum = 0

for line in lines:
  _, line = line.split('Game ')
  id, line = line.split(': ')
  id = int(id)
  draws = line.split('; ')

  valid = True
  
  for draw in draws:
    parts = draw.split(', ')
    for part in parts:
      n, color = part.split(' ')
      n = int(n)

      if color == 'blue':
        if n > 14:
          valid = False
      elif color == 'green':
        if n > 13:
          valid = False
      elif color == 'red':
        if n > 12:
          valid = False

  if valid:
    sum += id

print(sum)
'''

with open('input.txt', 'r') as f:
  lines = f.read().split('\n')

sum = 0

for line in lines:
  _, line = line.split('Game ')
  id, line = line.split(': ')
  id = int(id)
  draws = line.split('; ')

  bs, gs, rs = 0, 0, 0
  
  for draw in draws:
    parts = draw.split(', ')
    for part in parts:
      n, color = part.split(' ')
      n = int(n)

      if color == 'blue':
        if n > bs:
          bs = n
      elif color == 'green':
        if n > gs:
          gs = n
      elif color == 'red':
        if n > rs:
          rs = n

  sum += bs*gs*rs

print(sum)