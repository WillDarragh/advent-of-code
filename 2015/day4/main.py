# Advent of code 2015 Day 4

from hashlib import md5

with open('input.txt') as f:
  data = f.read()

part_1 = '''
hex = 'bgvyzdsv'

i = 0

while(True):
  test = hex + str(i)

  hash = md5(test.encode())

  if hash.hexdigest()[:5] == '00000':
    print(i)
    break

  i += 1
'''

hex = 'bgvyzdsv'

i = 0

while(True):
  test = hex + str(i)

  hash = md5(test.encode())

  if hash.hexdigest()[:6] == '000000':
    print(i)
    break

  i += 1