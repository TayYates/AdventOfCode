import numpy as np
import scipy.ndimage as nd

# place dataset into a 2d array of integers
smokeList = []
with open('../data/day09sample.txt', 'r') as file:
    for line in file.read().splitlines():
        smokeList.append(list(line))
smokeMap = np.asarray(smokeList, dtype=int)

##################################
# part 1

# method to perform checks on the surrounding points
def spotChecker(smokeMap, spot, x, y):
    # only consider applicable items (avoid adding empty edges)
    values = []
    if x != 0:
        values.append(smokeMap[x-1][y]) 
    if x != 4:
        values.append(smokeMap[x+1][y])
    if y != 0:
        values.append(smokeMap[x][y-1])
    if y != 9:
        values.append(smokeMap[x][y+1])
    # add to risk if spot is a minimum
    if spot < min(values):
        return spot + 1
    else:
        return 0

# main method part 1
def partOne(smokeMap):
    totalRisk = 0
    spotList = []
    for x in range(0, 5):
        for y in range(0, 10):
            # run the check on each point
            # I know this looks ugly, but we need spotRisk as an int for part one and its x,y coordinate for part 2
            spotRisk = spotChecker(smokeMap, smokeMap[x][y], x, y)
            if spotRisk > 0:
                spotList.append([x,y])
                totalRisk += spotRisk
    # answer part 1
    print(totalRisk)
    # this is for part 2 :)
    return spotList

##################################
# part 2

def percolate(smokeMap, basin, x, y):
    pass
    

def partTwo(smokeMap, minList):
    basins = []
    print(f"There are {len(minList)} basins")
    # use each min as a starting point for each basin
    for min in minList:
        basin = []
        # flood in all directions until you hit a 9
        basin = percolate(smokeMap, basin, min[0], min[1])
        print(basin)


partTwo(smokeMap, partOne(smokeMap))