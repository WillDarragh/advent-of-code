# Advent of Code 2022 Day 2

scores = {'X': 1, 'Y': 2, 'Z': 3}

change = {'A': 'X', 'B': 'Y', 'C': 'Z'}
loses = {'A': 'Z', 'B': 'X', 'C': 'Y'}
wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}

score = 0

with open('input.txt') as f:
  txt = f.read()

for line in txt.split('\n'):
  a, b = line.split(' ')

  if b == 'X':
    score += scores[loses[a]]
  elif b == 'Y':
    score += 3
    score += scores[change[a]]
  else:
    score += 6
    score += scores[wins[a]]
    


print(score)