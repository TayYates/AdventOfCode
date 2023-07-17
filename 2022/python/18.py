import numpy as np
import scipy.ndimage as ndi

# puzzle input - 3d coordinates in a grid
data = open("../data/18.txt").read().split("\n")

# not pythonic, but list comprehension didn't like what I was trying to do
xList, yList, zList = [], [], []
for line in data:
  x, y, z = [int(coord) for coord in line.split(",")]
  xList.append(x)
  yList.append(y)
  zList.append(z)
#print(xList, yList, zList)

# set the grid
grid = np.zeros((max(xList)+2, max(yList)+2, max(zList)+2))
for x, y, z in zip(xList, yList, zList):
  grid[x][y][z] = 1

surfaceArea = 0
for x, y, z in zip(xList, yList, zList):
  # check above
  if grid[x][y+1][z] == 0:
    surfaceArea += 1
  # check below
  if grid[x][y-1][z] == 0:
    surfaceArea += 1
  # check left
  if grid[x-1][y][z] == 0:
    surfaceArea += 1
  # check right
  if grid[x+1][y][z] == 0:
    surfaceArea += 1
  # check front
  if grid[x][y][z-1] == 0:
    surfaceArea += 1
  # check back
  if grid[x][y][z+1] == 0:
    surfaceArea += 1

# part 1 answer
print(surfaceArea)

# thanks to some solutions for leetcode 1020 I found on google, had never heard of ndi before this
bubbleSurfaceArea = 0
grid = ndi.binary_fill_holes(grid)
# check each axis for number of times that the value changes. This will be equal to the internal surface area
bubbleSurfaceArea += np.sum(np.abs(np.diff(grid, 1, 0, 0, 0)))
bubbleSurfaceArea += np.sum(np.abs(np.diff(grid, 1, 1, 0, 0)))
bubbleSurfaceArea += np.sum(np.abs(np.diff(grid, 1, 2, 0, 0)))

# part 2 answer
print(bubbleSurfaceArea)