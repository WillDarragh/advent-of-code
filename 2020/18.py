
def solve(problem):

  #print(problem)

  op_stack = []
  el_stack = []

  pos = 0

  while (pos < len(problem)):

    char = problem[pos]

    if char == ' ':

      pass
    
    elif char == '+' or char == '*':

      op_stack.append(char)

    elif char == '(':

      prob = ''

      i = 1

      pos += 1

      while (i > 0):

        char = problem[pos]

        prob += char

        if char == ')':

          i -= 1

        elif char == '(':

          i += 1

        pos += 1

      el_stack.append(solve(prob[:-1]))

    else:

      el_stack.append(int(char))

    pos += 1

  while(len(el_stack) > 1):

    el1 = el_stack.pop(0)
    el2 = el_stack.pop(0)
    op = op_stack.pop(0)

    #print(f"{el1} {op} {el2} = {eval(f'{el1}{op}{el2}')}")

    el_stack.insert(0, (eval(f'{el1}{op}{el2}')))

  return el_stack[0]

def solve2(problem):

  #print(problem)

  op_stack = []
  el_stack = []

  pos = 0

  while (pos < len(problem)):

    char = problem[pos]

    if char == ' ':

      pass
    
    elif char == '+' or char == '*':

      op_stack.append(char)

    elif char == '(':

      prob = ''

      i = 1

      pos += 1

      while (i > 0):

        char = problem[pos]

        prob += char

        if char == ')':

          i -= 1

        elif char == '(':

          i += 1

        pos += 1

      el_stack.append(solve2(prob[:-1]))

    else:

      el_stack.append(int(char))

    pos += 1

  while(len(el_stack) > 1):

    index = 0

    try:
      index = op_stack.index('+')
    except:
      pass

    el1 = el_stack.pop(index)
    el2 = el_stack.pop(index)
    op = op_stack.pop(index)

    #print(f"{el1} {op} {el2} = {eval(f'{el1}{op}{el2}')}")

    el_stack.insert(index, (eval(f'{el1}{op}{el2}')))

  return el_stack[0]

def part1(data):

  problems = data.split('\n')

  solutions = []
  
  for problem in problems:

    solutions.append(solve(problem))

  return sum(solutions) 

def part2(data):

  problems = data.split('\n')

  solutions = []
  
  for problem in problems:

    #print(problem)
    #print(solve2(problem))
    #print()

    solutions.append(solve2(problem))

  return sum(solutions) 
