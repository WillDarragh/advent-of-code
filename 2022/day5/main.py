# Advent of Code 2022 Day 5

with open('input.txt') as f:
  data = f.read()

crates, moves = data.split('\n\n')

crates_matrix = [[] for i in range(9)]

for line in crates.split('\n'):

  for i in range(9):

    j = 1+i*4
    
    if line[j] != ' ':

      crates_matrix[i].insert(0, line[j])

#print(crates_matrix)

for move in moves.split('\n'):

  #print(move)
  
  move_list = move.split(' ')

  #print(move_list)
  
  number = int(move_list[1])
  from_i = int(move_list[3]) - 1
  to_i = int(move_list[5]) - 1

  boxes = []
  
  for i in range(number):

    boxes.insert(0, crates_matrix[from_i].pop())

  crates_matrix[to_i] += boxes

for col in crates_matrix:

  print(col[-1],end='')

#print(crates_matrix)