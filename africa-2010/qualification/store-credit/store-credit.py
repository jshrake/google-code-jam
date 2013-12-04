import sys

def find_two_items(credit, items, num_items):
  # complexity O(num_items * log(num_items))
  # need to keep track of original indices of the sorted items
  indices = sorted(range(num_items), key = lambda k: items[k])
  items.sort()
  beg = 0
  end = -1
  while True:
    first = items[beg]
    last  = items[end]
    total = first + last
    if total == credit:
      ind1 = indices[beg] + 1
      ind2 = indices[num_items + end] + 1
      if ind1 < ind2:
        return ind1, ind2 
      return ind2, ind1
    elif total < credit:
      beg += 1
    elif total > credit:
      end -= 1


num_cases = int(sys.stdin.readline())
for case in range(1, num_cases + 1):
    credit = int(sys.stdin.readline())
    num_items = int(sys.stdin.readline())
    items = list(map(int, sys.stdin.readline().split()))
    item1, item2 = find_two_items(credit, items, num_items) 
    print("Case #" + str(case) + ":", item1, item2)

