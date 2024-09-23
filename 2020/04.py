
def part1(data):
    __import__('time').sleep(1)
    # Data is automatically read from 01.txt
    return "".join(reversed(data))

def isint(s):
  for c in s:
    if c not in '0123456789':
      return False
  return True

def ishex(s):
  for c in s:
    if c not in '0123456789abcdef':
      return False
  return True

def part2(data):

  data = data.split('\n\n')
  
  fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

  valid = 0

  for d in data:

    keyvals = d.split()

    D = dict()

    keys = [keyval.split(':')[0] for keyval in keyvals]

    for keyval in keyvals:

      key, val = keyval.split(':')

      D[key] = val

    for f in fields:

      if f not in keys:

        break
    
    else:

      hgt = D['hgt']
      try:
        ihgt = int(hgt[:-2])
      except:
        continue

      hcl = D['hcl']
      ecl = D['ecl']

      pid = D['pid']

      if 1920 <= int(D['byr']) <= 2002:
        if 2010 <= int(D['iyr']) <= 2020:
          if 2020 <= int(D['eyr']) <= 2030:
            if len(D['byr']) == len(D['iyr']) == len(D['eyr']) == 4:
              if (hgt[-2:] == 'in' and 59 <= ihgt <= 76) or (hgt[-2:]=='cm' and 150 <= ihgt <= 193):
                if hcl[0] == '#':
                  if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    if len(pid) == 9:
                      if isint(pid):
                        if ishex(hcl[1:]):



                          valid += 1

  return valid

'''
def part2(data):
  data = data.split('\n')
'''
