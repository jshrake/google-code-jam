import sys

mem_solutions = {}

def solver(cell_numbers, cell_range):
  if not cell_numbers:
    return 0;
  if cell_range in mem_solutions:
    return mem_solutions[cell_range]
  coins_for_this_range = cell_range[1] - cell_range[0]
  subproblems = []
  # iterate through each cell
  for cell_number in cell_numbers:
    # Partition the cell numbers and cell range 
    # on the current cell number and then solve
    # two subproblems
    idx = cell_numbers.index(cell_number)
    smaller_range = (cell_range[0], cell_number - 1)
    smaller_cells = cell_numbers[0:idx]
    larger_range  = (cell_number + 1, cell_range[1])
    larger_cells  = cell_numbers[idx+1:]
    smaller_solve  = solver(smaller_cells, smaller_range)
    larger_solve  = solver(larger_cells, larger_range)
    subproblems.append(smaller_solve + larger_solve)
  # solution is the current answer + the minimum answer of the 
  # subproblems we solved
  mem_solutions[cell_range] = coins_for_this_range + min(subproblems)
  return mem_solutions[cell_range] 


num_cases = int(sys.stdin.readline())
for case in range(1, num_cases + 1):
  P, Q = map(int, sys.stdin.readline().split())
  cells = list(map(int, sys.stdin.readline().split()))
  print("Case #" + str(case) + ":", solver(cells, (1, P)))
  mem_solutions = {}

