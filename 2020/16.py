
import numpy as np

def part1(data):

  fields, your_ticket, nearby_tickets = data.split('\n\n')

  all_ranges = set()

  for line in fields.split('\n'):
    
    _, ranges_string = line.split(': ')

    ranges = ranges_string.split(' or ')

    for r in ranges:

      mn, mx = map(int, r.split('-'))

      for x in range(mn, mx+1):

        all_ranges.add(x)

  error_rate = 0

  nearby_tickets_lines = nearby_tickets.split('\n')[1:]

  for line in nearby_tickets_lines:

    nums = list(map(int, line.split(',')))

    for num in nums:

      if num not in all_ranges:

        error_rate += num

  return error_rate

def part2(data):

  fields, your_ticket, nearby_tickets = data.split('\n\n')

  all_ranges = set()

  all_fields = {}

  fields_count = 0

  for line in fields.split('\n'):
    
    field_string, ranges_string = line.split(': ')

    ranges = ranges_string.split(' or ')

    all_fields[field_string] = set()

    for r in ranges:

      mn, mx = map(int, r.split('-'))

      for x in range(mn, mx+1):

        all_ranges.add(x)

        all_fields[field_string].add(x)

    fields_count += 1

  nearby_tickets_lines = nearby_tickets.split('\n')[1:]

  good_tickets = []

  for line in nearby_tickets_lines:

    nums = list(map(int, line.split(',')))

    for num in nums:

      if num not in all_ranges:

        break
    
    else:

      good_tickets.append(nums)

  tickets_array = np.array(good_tickets)

  #print(tickets_array)

  fields_found = []

  fields_not_found = list(all_fields.keys())

  while(fields_not_found):

    for col in range(fields_count):

      pos_fields = []

      for field in fields_not_found:

        for pos_val in tickets_array[:, col]:

          if pos_val not in all_fields[field]:

            break

        else:

          pos_fields.append([field, col])
      
      if len(pos_fields) == 1:

        fields_found.append(pos_fields[0])

        fields_not_found.remove(pos_fields[0][0])

  #print(fields_found)

  my_ticket = list(map(int, your_ticket.split('\n')[1].split(',')))

  answer = 1

  for field, col in fields_found:

    if field.startswith('departure'):

      answer *= my_ticket[col]

  return answer
