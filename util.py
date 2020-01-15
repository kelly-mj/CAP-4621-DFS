import math

# declare dictionaries
connections = {}
locations = {}

def setup():
  # read contents from "locations.txt" into a dictionary
  location = open("locations.txt").read().split("\n")
  for line in location:
    location = line.split(" ")
    locations[location[0]] = location[1:]
    
  # read contents of "connections.txt" into dictionary
  for line in open("connections.txt").read().split("\n"):
    l = line.split(" ")
    p = l[2:]
    p.sort()
    connections[l[0]] = p

def verifyInput(p):
  if p in locations.keys():
    return True
  else:
    return False
