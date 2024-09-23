# Advent of Code 2022 Day 8

from pprint import pprint

def check(r, c):
  
  global mat
  
  val = mat[r][c]
  
  # Check up
  r_cur = r
  c_cur = c

  r_cur -= 1
  
  while r_cur >= 0:

    if mat[r_cur][c_cur] >= val:
      break
    
    if r_cur == 0:
      return True
    
    r_cur -= 1
  
  # Check down
  r_cur = r
  c_cur = c

  r_cur += 1
  
  while r_cur <= len(mat)-1:

    if mat[r_cur][c_cur] >= val:
      break
    
    if r_cur == len(mat)-1:
      return True
    
    r_cur += 1

  # Check left
  r_cur = r
  c_cur = c

  c_cur -= 1
  
  while c_cur >= 0:

    if mat[r_cur][c_cur] >= val:
      break
    
    if c_cur == 0:
      return True
    
    c_cur -= 1
    
  # Check right
  r_cur = r
  c_cur = c

  c_cur += 1
  
  while c_cur <= len(mat[0])-1:

    if mat[r_cur][c_cur] >= val:
      break
    
    if c_cur == len(mat[0])-1:
      return True
    
    c_cur += 1

  return False

def check2(r, c):

  global high_score
  global mat
  
  val = mat[r][c]

  # Check up
  r_cur = r
  c_cur = c
  ups = 0

  highest = val
  
  r_cur -= 1
  while r_cur >= 0:
    
    if mat[r_cur][c_cur] >= val:
      ups += 1
      break

    if r-r_cur == 1:
      highest = mat[r_cur][c_cur]
      ups += 1
      r_cur -= 1
      
    else:
      if mat[r_cur][c_cur] >= highest:
        highest = mat[r_cur][c_cur]
        ups += 1
      r_cur -= 1

  #print('ups for',r,c,val)
  #print(ups)
      
  # Check down
  r_cur = r
  c_cur = c
  downs = 0

  highest = val
  
  r_cur += 1
  while r_cur <= len(mat)-1:
    
    if mat[r_cur][c_cur] >= val:
      downs += 1
      break

    if r_cur-r == 1:
      highest = mat[r_cur][c_cur]
      downs += 1
      r_cur += 1
      
    else:
      if mat[r_cur][c_cur] >= highest:
        highest = mat[r_cur][c_cur]
        downs += 1
      r_cur += 1
  
  #print('downs for',r,c,val)
  #print(downs)
        
  # Check left
  r_cur = r
  c_cur = c
  lefts = 0

  highest = val
  
  c_cur -= 1
  while c_cur >= 0:
    
    if mat[r_cur][c_cur] >= val:
      lefts += 1
      break

    if c-c_cur == 1:
      highest = mat[r_cur][c_cur]
      lefts += 1
      c_cur -= 1
      
    else:
      if mat[r_cur][c_cur] >= highest:
        highest = mat[r_cur][c_cur]
        lefts += 1
      c_cur -= 1
  
  #print('lefts for',r,c,val)
  #print(lefts)
      
  # Check right
  r_cur = r
  c_cur = c
  rights = 0

  highest = val
  
  c_cur += 1
  while c_cur <= len(mat[0])-1:
    
    if mat[r_cur][c_cur] >= val:
      rights += 1
      break

    if c_cur-c == 1:
      highest = mat[r_cur][c_cur]
      rights += 1
      c_cur += 1
      
    else:
      if mat[r_cur][c_cur] >= highest:
        highest = mat[r_cur][c_cur]
        rights += 1
      c_cur += 1
  
  #print('rights for',r,c,val)
  #print(rights)

  #print(r,c,val)
  #print(ups, lefts, downs, rights)
  
  score = ups*downs*rights*lefts

  print(score, end=' ')
  
  if score > high_score:
    high_score = score
      
def check3(r, c):

  global high_score
  global mat
  
  val = mat[r][c]

  # Check up
  r_cur = r
  c_cur = c
  ups = 0

  r_cur -= 1
  while r_cur >= 0:
    ups += 1
    if mat[r_cur][c_cur] >= val:
      break
    else:
      r_cur -= 1

  # Check left
  r_cur = r
  c_cur = c
  lefts = 0

  c_cur -= 1
  while c_cur >= 0:
    lefts += 1
    if mat[r_cur][c_cur] >= val:
      break
    else:
      c_cur -= 1

  # Check down
  r_cur = r
  c_cur = c
  downs = 0
  
  r_cur += 1
  while r_cur <= len(mat)-1:
    downs += 1
    if mat[r_cur][c_cur] >= val:
      break
    else:
      r_cur += 1

  # Check right
  r_cur = r
  c_cur = c
  rights = 0

  
  c_cur += 1
  while c_cur <= len(mat[0])-1:
    rights += 1
    if mat[r_cur][c_cur] >= val:
      break
    else:
      c_cur += 1

  #print(r,c,val)
  #print(ups, lefts, downs, rights)
  
  score = ups*downs*rights*lefts

  #print(score, end=' ')
  
  if score > high_score:
    high_score = score
      
with open('input.txt') as f:
  data = f.read()

mat = data.split('\n')

rows = len(mat)
cols = len(mat[0])

vis = 0

high_score = 0

for r in range(rows):
  for c in range(cols):
    check3(r, c)
  #print()

vis += 2*len(mat) + 2*len(mat[0]) - 4

print(high_score)
    