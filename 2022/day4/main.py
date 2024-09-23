# Advent of Code 2022 Day 4

with open('input.txt') as f:
  data = f.read()

count = 0

for line in data.split():

  a, b = line.split(',')

  a1, a2 = map(int, a.split('-'))
  b1, b2 = map(int, b.split('-'))

  print(a1, a2)
  print(b1, b2)

  if (a1 <= b1) and (a2 >= b2):
    count += 1
  elif (a1 >= b1) and (a2 <= b2):
    count += 1
  elif (a1 == b1) and (a2 == b2):
    count += 1
    print('y')
  elif (a2 >= b1) and (a1 <= b1):
    count += 1
    print('y')
  elif (a2 >= b2) and (a1 <= b2):
    count += 1
    print('y')
  else:
    print('n')

  print()
print(count)