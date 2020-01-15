import math

# declare dictionaries
connections = {}
locations = {}

# read contents from "locations.txt" into a dictionary
location = open("locations.txt").read().split("\n")
for line in location:
  location = line.split(" ")
  locations[location[0]] = location[1:]
  
# read contents of "connections.txt" into dictionary
c = open("connections.txt").read().split("\n")
for line in c:
  l = line.split(" ")
  connections[l[0]] = l[2:]
      
print(locations)
print("\n")
print(connections)