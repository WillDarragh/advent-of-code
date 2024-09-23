# Advent of code 2015 Day ?

with open('input.txt') as f:
  data = f.read()


part_1 = '''
total = 0

for line in data.split():
  x, y, z = map(int, line.split('x'))

  a = x*y
  b = y*z
  c = z*x

  smallest = min([a, b, c])

  total += 2*a + 2*b + 2*c + smallest

print(total)
'''

total = 0

for line in data.split():
  sides = list(map(int, line.split('x')))

  sides.sort()

  x, y, z = sides

  

  total += 2*x + 2*y + x*y*z

print(total)