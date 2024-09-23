from functools import total_ordering

RANKS = 'AKQT98765432J'

def five(hand):
  return hand.num_ranks == 1 or hand.num_ranks == 0

def four(hand):
  return any(hand.hand.count(rank) == 4 for rank in hand.ranks)

def full(hand):
  any_two = False
  any_three = False
  if hand.num_ranks == 2:
    for rank in hand.ranks:
      rank_count = hand.hand.count(rank)
      if rank_count == 2:
        any_two = True
      if rank_count == 3:
        any_three = True
  return any_two and any_three

def three(hand):
  return any(hand.hand.count(rank) == 3 for rank in hand.ranks)

def twopair(hand):
  return sum(hand.hand.count(rank) == 2 for rank in hand.ranks) == 2

def onepair(hand):
  return any(hand.hand.count(rank) == 2 for rank in hand.ranks)

def high(hand):
  return True

TYPE_FUNCS = [five, four, full, three, twopair, onepair, high]

def type_score(hand):
  for i, func in enumerate(TYPE_FUNCS):
    if func(hand):
      return i
  print('TYPE PROBLEM')
  return -1

def rank_score(rank):
  for i, r in enumerate(RANKS):
    if rank == r:
      return i
  print(r, rank, 'RANK PROBLEM')
  return -1
'''
five  0
four  1
full  2
three 3
two   4
one   5
high  6
'''

NAMES = 'five four full three two one high'.split()
PLUS_ONES = [6, 2]

@total_ordering
class Hand:
  hand: str
  ranks: list
  num_ranks: int
  type_score: int

  def __init__(self, hand):
    self.hand = hand
    self.ranks = list(set(hand)-{'J'})
    self.num_ranks = len(self.ranks)
    self.type_score = type_score(self)
    #if hand.count('J') > 1:
      #print(hand, 'before:', self.type_score, end=' ')
    for i in range(self.hand.count('J')):
      if self.type_score == 0:
        break
      elif self.type_score in PLUS_ONES:
        self.type_score -= 1
      else:
        self.type_score -= 2
    if hand.count('J') > 1:
      print(hand, NAMES[self.type_score])

  def __gt__(self, other):
    self_score = self.type_score
    other_score = other.type_score
    if self_score != other_score:
      return self_score < other_score
    for i in range(5):
      self_r = self.hand[i]
      other_r = other.hand[i]
      self_score = rank_score(self_r)
      other_score = rank_score(other_r)
      if self_score != other_score:
        return self_score < other_score
    return False
      
  def __eq__(self, other):
    return self.hand == other.hand  

with open('input.txt', 'r') as f:
  data = f.read()

hands_bids = []

for line in data.split('\n'):
  hand, bid = line.split()
  hand = Hand(hand)
  bid = int(bid)

  hands_bids.append([hand, bid])

hands_bids.sort(key=lambda x: x[0])

output = 0

for i, hand_bid in enumerate(hands_bids, 1):
  hand, bid = hand_bid
  output += i * bid
print(output)