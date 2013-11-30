import sys

def is_bipartite(graph, v, color, coloring):
  coloring[v] = color 
  for node in graph[v]:
    if node not in coloring and not is_bipartite(graph, node, not color, coloring):
      return False
    elif coloring.get(node) == color:
      return False
  return True

num_cases = int(sys.stdin.readline())
for case in range(1, num_cases + 1):
  M = int(sys.stdin.readline())
  graph = {}
  for k in range(0, M):
    names = list(map(str, sys.stdin.readline().split()))
    graph.setdefault(names[0], []).append(names[1])
    graph.setdefault(names[1], []).append(names[0])
  coloring = {}
  output = "Yes"
  for node in graph.keys():
    if node not in coloring and not is_bipartite(graph, node, True, coloring):
        output = "No"
        break
  print("Case #" + str(case) + ":", output)

