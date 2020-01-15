# declare dictionaries
connections = {}
locations = {}

def setup():
  # read contents of "connections.txt" into dictionary
  c = open("connections.txt").read().split("\n")
  for line in c:
    l = line.split(" ")
    connections[l[0]] = l[2:]

  print(connections)