from math import inf

def convert(x, mapping):
  for m in mapping:
    dest, source, rang = list(map(int, m.split()))
    if source <= x < source+rang:
      return dest + x-source
  return x

def make_low_highs(l):
  low_highs = []
  for x in l:
    dest, source, rang = x
    destl, desth = dest, dest+rang-1
    sourcel, sourceh = source, source+rang-1
    low_highs.append([sourcel, sourceh, destl, desth])

  low_highs.sort(key=lambda x: x[0])

  return low_highs

def add_difs(l):
  return [x + [(x[2]-x[0])] for x in l]

def split_ints(l):
  return [list(map(int, x.split())) for x in l]

def fix(l):
  return add_difs(make_low_highs(split_ints(l)))

def ranges_converted(ranges, mapping):
  
  new_ranges = []
  
  lowest = mapping[0][0]
  highest = mapping[-1][1]
  
  for rang in ranges:
    low, high = rang

    curr_low = low
    
    # Lower than lowest mapping
    if low < lowest:
      if high < lowest:
        new_ranges.append([low, high])
        continue
      else:
        new_ranges.append([low, lowest-1])
        curr_low = lowest
    # Within mapping
    #############################
    for m in mapping:
      sl, sh, dl, dh, dif = m
      if curr_low > sh:
        continue
      else:
        if high <= sh:
          newl = curr_low+dif
          newh = high+dif
          new_ranges.append([newl, newh])
          break
        else:
          newl = curr_low+dif
          newh = dh
          new_ranges.append([newl, newh])
          curr_low = sh+1
  
  
    ###############################
    # Higher than highest mapping
    if curr_low > highest:
      new_ranges.append([curr_low, high])
  
  return new_ranges

with open('input.txt', 'r') as f:
  data = f.read()

_, data = data.split('seeds: ')

seeds, data = data.split('\n\nseed-to-soil map:\n')
seeds = list(map(int, seeds.split()))
pairs = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]

s2s, data = data.split('\n\nsoil-to-fertilizer map:\n')
s2s = s2s.split('\n')
s2f, data = data.split('\n\nfertilizer-to-water map:\n')
s2f = s2f.split('\n')
f2w, data = data.split('\n\nwater-to-light map:\n')
f2w = f2w.split('\n')
w2l, data = data.split('\n\nlight-to-temperature map:\n')
w2l = w2l.split('\n')
l2t, data = data.split('\n\ntemperature-to-humidity map:\n')
l2t = l2t.split('\n')
t2h, h2l = data.split('\n\nhumidity-to-location map:\n')
t2h = t2h.split('\n')
h2l = h2l.split('\n')

print('here')

lowest = inf

'''
for seed in seeds:
  x = seed
  for mapping in [s2s, s2f, f2w, w2l, l2t, t2h, h2l]:
    x = convert(x, mapping)

  if x < lowest:
    lowest = x
'''

s2s = fix(s2s)
s2f = fix(s2f)
f2w = fix(f2w)
w2l = fix(w2l)
l2t = fix(l2t)
t2h = fix(t2h)
h2l = fix(h2l)

for p in pairs:
  low, rang = p
  high = low + rang-1
  ranges = [[low, high]]
  for mapping in [s2s, s2f, f2w, w2l, l2t, t2h, h2l]:
    ranges = ranges_converted(ranges, mapping)
    ranges.sort(key=lambda x: x[0])
  
  x = ranges[0][0]
  if x < lowest:
    lowest = x

print(lowest)