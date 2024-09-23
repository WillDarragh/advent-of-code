
def race_dist(time, hold):
  time_left = time-hold
  return hold*time_left
  

with open('input.txt', 'r') as f:
  data = f.read()

''''
time, dist = data.split('\n')
_, time = time.split(':')
time = time.strip()
_, dist = dist.split(':')
dist = dist.strip()

times = list(map(int, time.split()))
dists = list(map(int, dist.split()))

races = list(zip(times, dists))

output = 1

for race in races:
  t, record = race

  ways = 0
  
  for i in range(1,t):

    d = race_dist(t, i)

    if d > record:
      ways += 1

  output *= ways

print(output)
'''

time, dist = data.split('\n')
_, time = time.split(':')
time = time.strip()
_, dist = dist.split(':')
dist = dist.strip()

times = time.split()
dists = dist.split()
time = int(''.join(times))
dist = int(''.join(dists))

check = 1

output = 0
for i in range(1,time):

  d = race_dist(time, i)

  if d > dist:
    output += 1

print(output)