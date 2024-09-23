
from pprint import pprint

from functools import lru_cache

def solve_rule(rule):

  if '|' in rule:

    rule1, rule2 = rule.split(' | ')

    return {'l':solve_rule(rule1), 'r':solve_rule(rule2)}

  else:

    nums = rule.split()

    return list(map(lambda n: solve_helper(n), nums))

@lru_cache
def solve_helper(num):

  global rules_dict

  rule = rules_dict[num]

  if rule[0] == '\"':

    return rule[1]

  else:
    
    return solve_rule(rule)

def find_all(rule_path):

  global strings

  pprint(rule_path)
  print()

  for i, part in enumerate(rule_path):

    if isinstance(part, dict):

      new_path = list(rule_path)

      for opt in ['l', 'r']:

        new_path[i] = list(part[opt])

        find_all(new_path)

    elif isinstance(part, list):

      find_all(part)


def part1(data):

  global rules_dict, strings

  rules, messages = data.split('\n\n')

  rules_dict = {}

  for rule in rules.split('\n'):

    rule_num, rule_expression = rule.split(': ')

    rules_dict[rule_num] = rule_expression

  rule_path = solve_rule(rules_dict['0'])
  
  strings = []

  find_all(rule_path)

  print(strings)

def part2(data):

  pass
