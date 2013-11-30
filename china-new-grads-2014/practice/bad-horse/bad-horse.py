import sys

def is_bipartite(graph, v, color, coloring):
  coloring[v] = color 
  # iterate through adjacent nodes and look for any nodes
  # that have a coloring that does not match our expectation
  # that adjacent nodes have an opposite color of our current
  # node
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
  # iterate through all nodes in the graph
  # graph may not be connected
  # look for any indication that the graph is not bipartite
  for node in graph.keys():
    if node not in coloring and not is_bipartite(graph, node, True, coloring):
        output = "No"
        break
  print("Case #" + str(case) + ":", output)

