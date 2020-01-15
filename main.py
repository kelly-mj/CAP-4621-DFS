import util as util

# import/parse location and connection file contents
util.setup()

# TODO: prompt user for input
# test input
start = "A1"
end   = "G1"

# do DFS to find path from start to end
path = [start]
visited = [start]

while(path[-1] != end):
  change = 0  # flag to indicate whether any unvisited neighbors were found
  # iterate over neighbors of current node
  for x in util.connections[path[-1]]:
    # if neighbor has not been visited yet, add neighbor to the path
    if x not in visited:
      curr = x
      visited.append(x)
      path.append(x)
      change = 1
      break
  # if no unvisited neighbors were found, pop current node from the stack
  if change == 0:
    path.pop()

print(path)