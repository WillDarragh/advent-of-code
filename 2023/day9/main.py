from pprint import pprint

with open('input.txt') as f:
  data = f.read()

total = 0

for line in data.split('\n'):

  seqs = []
  curr_s = list(map(int, line.split()))
  seqs.append(curr_s)
  
  while(any(n != 0 for n in curr_s)):
    new_s = []
    for i in range(len(curr_s)-1):
      new_s.append(curr_s[i+1]-curr_s[i])
    curr_s = new_s
    seqs.append(curr_s)

  dif = 0
  for s in seqs[::-1]:
    dif = s[0] - dif

  total += dif

print(total)