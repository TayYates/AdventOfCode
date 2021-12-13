import numpy as np

# place dataset into a 2d array of integers
octopi = []
with open('../data/day11.txt', 'r') as file:
    for line in file.read().splitlines():
        octopi.append(list(line))
octoMap = np.asarray(octopi, dtype=int)

neighbors = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, +1],
    [1, -1],
    [1, 0],
    [1, 1],
]

# boolean check if the point in question is inside the grid. Edges return False, good points return True
def checkEdge(x, y):
    if (x > -1) and (x < 10) and (y > -1) and (y < 10):
        return True

# this one does the heavy lifting for each flash step
def checkFlashes(octoMap, neighbors):
    flashes = []
    for y in range(0, 10):
        for x in range(0, 10):
            # iterate over each octopus in the grid, adding one and checking for a 10
            octoMap[y][x] += 1
            if octoMap[y][x] == 10:
                # if octopus is a 10, reset it to zero and add it to the list of flashes
                octoMap[y][x] = 0
                flashes.append([y,x])
    for flash in flashes:
        for neighbor in neighbors:
            # operate on all neighbors, if they flash, add them to the list as well
            spot = [(flash[0] + neighbor[0]),(flash[1] + neighbor[1])]
            # confirm that the spot is inside the map and hasn't already flashed this round
            if checkEdge(spot[0], spot[1]):
                if octoMap[spot[0], spot[1]] != 0:
                    # +1 to the spot, and check if it also flashes
                    octoMap[spot[0], spot[1]] += 1
                    if octoMap[spot[0], spot[1]] == 10:
                        # if the spot flashes, bring it back to zero and adding it to the list
                        octoMap[spot[0], spot[1]] = 0
                        flashes.append(spot)
    return len(flashes), octoMap

# part 1 driver
def part1(octoMap, neighbors):
    flashCount = 0
    for step in range(0, 100):
        newFlashes, octoMap = checkFlashes(octoMap, neighbors)
        flashCount += newFlashes
    return flashCount

def part2(octoMap, neighbors):
    # no need to redo steps 1-100. Just start with the octoMap from part 1 and continue
    step = 100
    while True:
        step += 1
        newFlashes, octoMap = checkFlashes(octoMap, neighbors)
        # if a step gives 100 flashes, that means every octopus flashed and they're in sync
        if newFlashes == 100:
            return (step)

print(part1(octoMap, neighbors))
print(part2(octoMap, neighbors))