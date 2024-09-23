
D = {}

def recursive(bag):

  global D

  if 'shiny gold' in D[bag]:

    return True

  for bs in D[bag]:

    if bs != 'other':

      if recursive(bs):

        return True
  
  return False

def recursive2(bag):

  global D

  #print(D[bag])

  if D[bag] == ['no other']:
    return 1

  count = 1

  for b in D[bag]:

      num = int(b.split()[0])

      bn = ' '.join(b.split()[1:])

      #print(bn)

      for n in range(num):

        c = recursive2(bn)

        #print(c)

        count += recursive2(bn)

  return count

def part1(data):
  global D
  data = data.split('\n')

  things, contains = [], []

  for d in data:

    t, c = d.split(' bags contain ')

    things.append(t)

    cs = c.split(', ')

    cs = [' '.join(C.split()[1:-1]) for C in cs]

    contains.append(cs)

  #for t, c in zip(things, contains):
  #  print(t, c)

  D = {t:c for t,c in zip(things, contains)}

  count = 0

  for thing in things:

    if recursive(thing):

      count += 1
      
  return count



def part2(data):
  global D
  data = data.split('\n')

  things, contains = [], []

  for d in data:

    t, c = d.split(' bags contain ')

    things.append(t)

    cs = c.split(', ')

    cs = [' '.join(C.split()[:-1]) for C in cs]

    contains.append(cs)

  #for t, c in zip(things, contains):
  #  print(t, c)

  D = {t:c for t,c in zip(things, contains)}

  return recursive2('shiny gold')-1