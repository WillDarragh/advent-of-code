# Advent of code 2015 Day ?

with open('input.txt') as f:
  data = f.read()

part1 = '''
floor = data.count('(') - data.count(')')

print(floor)
'''

position = 0

for i, c in enumerate(data, 1):
  if c == '(':
    position += 1
  else:
    position -= 1
  if position == -1:
    print(i)
    break