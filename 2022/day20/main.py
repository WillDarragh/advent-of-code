# Advent of Code 2022 Day 20

class Node:

  def __init__(self, id, n):

    self.prev = None
    self.next = None
    self.id = id
    self.n = n

class Linked:

  def __init__(self):

    self.first = None
    self.last = None

  def find(self, id, n):

    curr = self.first

    while (id, n) != (curr.id, curr.n):
      curr = curr.next

    return curr

  def add(self, node):

    if not self.first:

      self.first = node
      self.last = node
      node.next = node
      node.prev = node

    else:

      self.last.next = node
      self.first.prev = node
      node.prev = self.last
      self.last = node
      node.next = self.first

  def solve(self):

    curr = self.first

    while curr.n != 0:
      curr = curr.prev

    S = 0
    
    for i in range(3):
      for j in range(1000):
        curr = curr.next
      S += curr.n

    return S

  def length(self):

    l = 1
    
    first = self.first
    curr = first.next

    while (curr != first):
      curr = curr.next
      l += 1

    return l
  
  def print(self):

    n = 1
    
    first = self.first
    curr = first.next

    print(first.n, end=' ')
    
    while (curr != first):

      print(curr.n, end=' ')

      curr = curr.next

      n += 1

    print()

with open('input.txt') as f:
  data = f.read()

original = []

linked = Linked()

id = 0
for line in data.split('\n'):
  original.append((id, int(line)))
  
  linked.add(Node(id, int(line)))

  id += 1

mod = len(original)

print('Mixing...')
print()

for id, n in original:

  node = linked.find(id, n)

  new = node
  
  if n > 0:
    for i in range(n):
      new = new.next

    node.prev.next = node.next
    node.next.prev = node.prev

    node.next = new.next
    new.next.prev = node
    node.prev = new
    new.next = node

  elif n < 0:
    for i in range(abs(n)):
      new = new.prev
      
    node.prev.next = node.next
    node.next.prev = node.prev

    node.prev = new.prev
    new.prev.next = node
    node.next = new
    new.prev = node

print('Solving...')
print()

print(linked.solve())