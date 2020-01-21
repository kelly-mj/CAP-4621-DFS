import util as util
import math

# import/parse location and connection file contents
util.setup()

#Receive the input from the user for the starting and ending cities
temp = input("What is the starting city? ")
while(util.verifyInput(temp)!=True):
      print("\nPlease input a valid city")
      temp = input("What is the starting city? ")
start = temp

temp   = input("\nWhat is the ending city? ")
while(util.verifyInput(temp)!=True):
      print("\nPlease input a valid city")
      temp = input("What is the ending city? ")
end = temp

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

#outside of for loop in order to be unchanging with each loop
sum=0
#you need to run through the path path.length()-1 times
for i in range(0, len(path)-1):
      #reinitializes the array each time it loops.
      points = []
      
      #gets the first element in the pair
      for value in util.locations[path[i]]:
            points.append(value)
      #gets the second element in the pair
      for value in util.locations[path[i+1]]:
            points.append(value)
      
      #assigns the corresponding variable
      x1 = int(points[0])
      x2 = int(points[2])
      y1 = int(points[1])
      y2 = int(points[3])
      
      #calculates distance
      distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
      print(path[i] + " to " + path[i+1] + " length " + "%.2f" %distance)
      sum = sum + distance

print("Total path length %.2f"  %sum)