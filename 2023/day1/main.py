from math import inf

NUMS = 'one.two.three.four.five.six.seven.eight.nine'.split('.')
RNUMS = [N[::-1] for N in NUMS]
DIGS = '123456789'

TODIG1 = dict(zip(NUMS, DIGS))
TODIG2 = dict(zip(RNUMS, DIGS))
TODIG = TODIG1 | TODIG2

def first_digit(word):
  first = ''
  loc = inf
  for N in NUMS:
    if N in word:
      Nloc = word.find(N)
      if Nloc < loc:
        first = TODIG[N]
        loc = Nloc
  for D in DIGS:
    if D in word:
      Dloc = word.find(D)
      if Dloc < loc:
        first = D
        loc = Dloc
  return first
      

def last_digit(word):
  word = word[::-1]
  last = ''
  loc = inf
  for N in RNUMS:
    if N in word:
      Nloc = word.find(N)
      if Nloc < loc:
        last = TODIG[N]
        loc = Nloc
  for D in DIGS:
    if D in word:
      Dloc = word.find(D)
      if Dloc < loc:
        last = D
        loc = Dloc
  return last

with open('input.txt', 'r') as f:
  data = f.read()

lines = data.split('\n')

sum = 0

for line in lines:
  a,b = first_digit(line), last_digit(line)
  num = int(a + b)
  sum += num

print(sum)