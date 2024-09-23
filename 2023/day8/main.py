from pprint import pprint
from time import sleep
from math import lcm

LR = {'L':0, 'R':1}

A = 'AAA'
Z = 'ZZZ'

with open('input.txt', 'r') as f:
  data = f.read()

LRS, nodes_data = data.split('\n\n')
LRMOD = len(LRS)

nodes = {}
for line in nodes_data.split('\n'):
  node, children_data = line.split(' = (')
  children_data = children_data[:-1]
  child_a, child_b = children_data.split(', ')
  nodes[node] = (child_a, child_b)

'''
i = 0
curr = A

steps = 0

while(curr != Z):
  lri = i % LRMOD

  lr = LR[LRS[lri]]
  
  curr = nodes[curr][lr]

  steps += 1
  i += 1

print(steps)
'''

curr_list = []
for node in nodes:
  if node[-1] == 'A':
    curr_list.append(node)

cycles = []

for node in curr_list:
  i = 0
  steps = 0
  curr = node
  
  while(curr[-1] != 'Z'):
    lri = i % LRMOD
    lr = LR[LRS[lri]]

    curr = nodes[curr][lr]

    steps += 1
    i += 1

  cycles.append(steps)

print(lcm(*cycles))