import networkx as nx

text = [(ord(x)) for x in open("../data/12.txt").read() if x != '\n']
list = [[] for _ in range(len(text))]
# store the locations of the start and end, and then replace them with 'a' and 'z' ord values
S, E = text.index(83), text.index(69)
text[S], text[E] = 97, 122

# build the list of edges for each node
graph = nx.DiGraph()

for i in range(0, len(text)):
  if i >= 61:
    # can it move up?
    if abs(text[i] - text[i-61]) <= 1 or text[i] > text[i-61]:
      graph.add_edge(i, i-61)
  if i < 2440:
    # can it move down?
    if abs(text[i] - text[i+61]) <= 1 or text[i] > text[i+61]:
      graph.add_edge(i, i+61)
  if i % 61 != 0:
    # can it move left?
    if abs(text[i] - text[i-1]) <= 1 or text[i] > text[i-1]:
      graph.add_edge(i, i-1)
  if i % 61 != 60:
    # can it move right?
    if abs(text[i] - text[i+1]) <= 1 or text[i] > text[i+1]:
      graph.add_edge(i, i+1)
#print(graph)

# work smart, not hard
Soln = nx.shortest_path_length(graph, target = E)

# part 1 answer
print(Soln.get(S))

# get the path lengths of every tile that has a height of 'a'
routes = [Soln.get(i) for i in range(len(text)) if text[i] == 97]
# only keep the ones that have a valid route to E
routes = [r for r in routes if r != None]

# part 2 answer
print(min(routes))