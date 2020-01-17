import util as util
import math
# import/parse location and connection file contents
util.setup()

# TODO: prompt user for input
# test input
start = "A1"
end   = "G1"

# do DFS to find path from start to end
path = [start]
visited = [start]
distances = []

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

for i in range(0, len(path)-1):
      points = []
      for value in util.locations[path[i]]:
            points.append(value)
      for value in util.locations[path[i+1]]:
            points.append(value)
      x1 = int(points[0])
      x2 = int(points[2])
      y1 = int(points[1])
      y2 = int(points[3])
      distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
      distances.append(distance)
      #print(points)
#print(distances)
sum = 0
for i in distances:
      sum = sum + i
      
print(sum)
            
            
#print(path)