# Advent of Code 2022 Day 7

TOTAL = 0

PART2 = 999999999999999999

class DirTree:
  
  def __init__(self, name, value=None, parent=None):
    self.parent = parent
    self.name = name
    self.value = value
    self.children = []
  def add(self, name, value=None):
    node = DirTree(name, parent=self, value=value)
    self.children.append(node)
  def report(self):
    print(self.name)
    if self.value:
      print(self.value)
    for node in self.children:
      node.report()
  def goto(self, name):
    for node in self.children:
      if node.name == name:
        return node
  def total_size(self):
    if self.value:
      return(self.value)
    else:
      total = 0
      for node in self.children:
        total += node.total_size()
      return total
  def solve(self):
    global TOTAL
    if not self.value and self.total_size() <= 100000:
      TOTAL += self.total_size()
    for node in self.children:
      node.solve()
  def solve2(self):
    global min_remove, PART2
    if self.total_size() >= min_remove:
      if self.total_size() < PART2:
        PART2 = self.total_size()
    for node in self.children:
      node.solve2()
      
with open('input.txt') as f:
  data = f.read()

dir_dict = {'/': {}}

lines = data.split('\n')

num_lines = len(lines)

line_num = 0

tree = DirTree('/')

curr = tree

while(line_num) < num_lines:
  
  line = lines[line_num]

  #print(line_num, line)
  
  if line.startswith('$ cd /'):

    curr = tree

    line_num += 1

  elif line.startswith('$ cd ..'):

    curr = curr.parent

    line_num += 1
  
  elif line.startswith('$ cd'):

    _, _, dir = line.split()

    for node in curr.children:
      if dir == node.name:
        break
    else:
      curr.add(dir)

    curr = curr.goto(dir)

    line_num += 1

  elif line.startswith('$ ls'):

    line_num += 1

    next_line = lines[line_num]

    while not next_line.startswith('$'):

      a, b = next_line.split()

      if a == 'dir':
        curr.add(b)
      else:
        curr.add(b, value=int(a))

      line_num += 1

      if line_num >= num_lines: 
        break
      
      next_line = lines[line_num]

total = 70000000
needed= 30000000
used = tree.total_size()
free = total - used
min_remove = needed - free

tree.solve2()

print(PART2)

