# Advent of Code 2022 Day 11

from math import floor

class Monkey:

  def __init__(self, items, op, test, if_true, if_false):
    self.items = items
    self.op = op
    self.test = test
    self.if_true = if_true
    self.if_false = if_false

    self.inspected = 0

  def add(self, item):
    self.items.append(item)
  
  def turn(self):
    global monkeys, mod

    for item in self.items:

      old = item

      #print(old)
      
      self.inspected += 1
      
      #print(op)

      op = self.op.replace('old', str(old))

      new = eval(op)

      #new = floor(new/3)
      new = new%mod

      #print(new)
      
      if new%self.test == 0:

        monkeys[self.if_true].add(new)

      else:

        monkeys[self.if_false].add(new)

    self.items = []
  
  def print(self):
    print(self.items)

  def inspected(self):
    print(self.inspected)

with open('input.txt') as f:
  data = f.read()

monkeys = []

for m in data.split('\n\n'):
  lines = m.split('\n')

  _, items_string = lines[1].split(':')
  items = list(map(int, items_string.split(', ')))

  _, op = lines[2].split('= ')

  _, test = lines[3].split('by ')
  test = int(test)

  _, if_true = lines[4].split('monkey ')
  if_true = int(if_true)

  _, if_false = lines[5].split('monkey ')
  if_false = int(if_false)

  monkeys.append(Monkey(items, op, test, if_true, if_false))

tests = [m.test for m in monkeys]

mod = 1

for t in tests:

  mod *= t

for round in range(10000):

  if round%100 == 0:
    print(round)
  
  for m in monkeys:
    m.turn()

for m in monkeys:

  #print(m.items)
  print(m.inspected)

inspecteds = [m.inspected for m in monkeys]

inspecteds.sort()

print(inspecteds)
print(inspecteds[-1] * inspecteds[-2])