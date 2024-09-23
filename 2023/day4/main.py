from functools import cache

with open('input.txt', 'r') as f:
  lines = f.read().split('\n')

'''
total = 0

for line in lines:
  _, line = line.split(': ')
  p1, p2 = line.split(' | ')

  winning = list(map(int, p1.split()))

  mine = list(map(int, p2.split()))

  points = 0
  
  for m in mine:
    if m in winning:
      if not points:
        points = 1
      else:
        points *= 2

  total += points

print(total)
'''

cards = {}
total = 0

for i, line in enumerate(lines, 1):
  _, line = line.split(': ')
  p1, p2 = line.split(' | ')

  winning = list(map(int, p1.split()))

  mine = list(map(int, p2.split()))

  cards[i] = [winning, mine]

@cache
def process(i):
  global cards
  num = 1

  copies = 0
  winning, mine = cards[i]
  for m in mine:
    if m in winning:
      copies += 1

  for c in range(copies):
    num += process(i+1+c)

  return num

for i in cards:
  total += process(i)

print(total)