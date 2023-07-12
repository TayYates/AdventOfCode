# sand initiates at 500,0
# one sand falls at a time, and 2nd sand doesn't start falling until the previous has hit it's resting place
# if blocked, it tries down+left. If that's blocked, it tries down+right. It continues to move until it no longer can
# using the puzzle input, how many units fall before the flow becomes an infinite loop?

import numpy as np

input = open("../data/14.txt").read().split("\n")
caveMap = np.zeros((200, 800), dtype=int)

# fill the caveMap in with the stone from the puzzle input
for line in input:
  commands = line.split(" -> ")
  lastPos = commands[0].split(",")
  for c in commands[1:]:
    x1, y1 = int(lastPos[0]), int(lastPos[1])
    x2, y2 = int(c.split(",")[0]), int(c.split(",")[1])
    # if true, then we're drawing along on the x axis
    if abs(x1-x2) != 0:
      x1, x2 = min(x1, x2), max(x1, x2)
      caveMap[y1, x1:x2+1] = 1
    else:
      y1, y2 = min(y1, y2), max(y1, y2)
      caveMap[y1:y2+1, x1] = 1
    lastPos = c.split(",")

# find the highest y corrdinate that has a value of 1
ceiling = max(np.where(caveMap == 1)[0])+2
# arbitrary number. If your answer equals this, increase the range until the answer stops changing
for i in range(810):
  currPos = [1, 500]
  # yes I know this isn't best practice, but the numpy array has a limited size and there's a guaranteed break point
  while True:

    # if not already blocked, move down as far as possible
    if caveMap[currPos[0]+1, currPos[1]] == 0 and currPos[0] < ceiling:
      # Extremely inefficient, TODO speed this up
      currPos[0] += 1

    # try to move down+left
    elif caveMap[currPos[0]+1, currPos[1]-1] == 0 and currPos[0] < ceiling:
      currPos[0], currPos[1] = currPos[0]+1, currPos[1]-1

    # try to move down+right
    elif caveMap[currPos[0]+1, currPos[1]+1] == 0 and currPos[0] < ceiling:
      currPos[0], currPos[1] = currPos[0]+1, currPos[1]+1
      
    # if you get here *and* you're blocked, you've hit your resting place. Update the caveMap with currPos and break the whileTrue        
    elif currPos[0] < ceiling: 
      caveMap[currPos[0], currPos[1]] = 2
      break

    # these never get blocked. It's in freefall, so you need to break the for loop here
    else:
      break

# part 1 answer
print(np.sum(caveMap == 2))


########################## part 2 version, running separately to keep it cleaner ############################

# remove the rocks from part 1
caveMap[np.where(caveMap == 2)] = 0

# find the highest y corrdinate that has a value of 1, and set the values of the whole row 2 above it to 1
ceiling = max(np.where(caveMap == 1)[0])+2
caveMap[ceiling, :] = 1
# I used this number to go back and reduce the size of the numpy array
#print(ceiling)

# arbitrary number. If your answer equals this, increase the range until the answer stops changing
for i in range(27000):
  currPos = [0, 500]
  # yes I know this isn't best practice, but the numpy array has a limited size and there's a guaranteed break point
  while True:

    # if not already blocked, move down as far as possible
    if caveMap[currPos[0]+1, currPos[1]] == 0 and currPos[0] < ceiling:
      # Extremely inefficient, TODO speed this up by identifying the landing point instead of going 1 at a time
      currPos[0] += 1

    # try to move down+left
    elif caveMap[currPos[0]+1, currPos[1]-1] == 0 and currPos[0] < ceiling:
      currPos[0], currPos[1] = currPos[0]+1, currPos[1]-1

    # try to move down+right
    elif caveMap[currPos[0]+1, currPos[1]+1] == 0 and currPos[0] < ceiling:
      currPos[0], currPos[1] = currPos[0]+1, currPos[1]+1
      
    # if you get here, you've hit your resting place. Update the caveMap with currPos and break the whileTrue        
    else:
      caveMap[currPos[0], currPos[1]] = 2
      break

# visual test when using the sample data
#print(caveMap[0:13, 490:508])

# part 2 answer
print(np.sum(caveMap == 2))