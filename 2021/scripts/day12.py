from collections import defaultdict

#########################
# data prep

smalls = {} # format - 'name': number of times passed
larges = {} # format - 'name': number of times passed
routes = defaultdict(list) # format - 'point': list of points it can travel to
with open('../data/day12.txt', 'r') as file:
    for line in file.read().splitlines():
        items = list(line.split("-"))
        # fill in the routes dictionary using the given data
        routes[items[0]].append(items[1])
        routes[items[1]].append(items[0])
        for item in items:
            # build separate dictionaries for large caves and small caves (start/end count as small caves)
            if item.isupper():
                larges[item] = 0
            else:
                smalls[item] = 0
# prime the dictionary so that it can never go back to 'start'
smalls['start'] += 1

#########################
# part 1

# credit to https://www.python.org/doc/essays/graphs/ for saving my ass on this one
# find_all_paths() in the official docs just needed mild tweaking

def pathfindAllPaths(routes, start, end, path = []):
    # path.append(start) does not work here, you need a list of lists instead
    path = path + [start]
    # if you found a way home, stop here and return your path
    if start == end:
        return [path]
    paths = []
    # go through every cave in the starting cave's list of possible targets
    for cave in routes[start]:
        # if you haven't already been there OR if it's a large cave, go ahead
        if cave not in path or cave not in smalls:
            # recursion, using the current cave as a new starting point, passing the current path as well
            newPaths = pathfindAllPaths(routes, cave, end, path)
            # take all the recursive new paths and add them to the final list of paths
            for newPath in newPaths:
                paths.append(newPath)
    return paths

pathList = pathfindAllPaths(routes, 'start', 'end')
print(len(pathList))

#########################
# part 2

