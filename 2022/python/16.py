import re
import networkx as nx
from itertools import permutations
from functools import lru_cache

data = open("../data/16-sample.txt").read().split("\n")
regEx = re.compile(r"^Valve (\w+) has flow rate=(\d+); \w+ \w+ to \w+ (.*)$")

G = nx.Graph()
possibleTargets = []

for line in data:
  valve, flow, options = regEx.match(line).groups()
  G.add_node(valve, flow = int(flow))
  for option in options:
    G.add_edge(valve, option)
  
  if int(flow) > 0: possibleTargets.append(valve)


def calcPotential(flow, timeRemaining):
  return flow * timeRemaining

def distanceDict(G, possibleTargets):
  distances = {}
  for source in possibleTargets:
    for target in possibleTargets:
      if source != target:
        distances[source, target] = nx.shortest_path_length(G, source, target)
  return distances

# recursive method to return a list of every route that passes the time limit
def routeChecker(start, timeBudget, state):
  routes = []
  for valve in possibleTargets:
    timeBudget -= nx.shortest_path_length(G, source = start, target = valve)
    timeBudget -= 1
    if state or timeBudget <= 0:
      continue
    routeChecker()

# this method returns the score of any given route
def getScore(G, start, route, timeBudget):
  # ok, now we need to calculate the time spent and the score of each route
  timeSpent = 0
  score = 0
  for dest in route:
    # spend time to walk to that valve
    timeSpent += nx.shortest_path_length(G, source = start, target = dest)
    # spend 1 minute to open it
    timeSpent += 1
    # calc the score that this valve will give you
    score += calcPotential(G.nodes[dest]['flow'], timeBudget-timeSpent-1)
  return score

distDict = distanceDict(G, possibleTargets)

# TODO not done yet