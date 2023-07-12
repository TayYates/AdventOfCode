# integer values only
# sensors know where the closest beacon is
# there could be other beacons outside of the radius created by the "closest beacon"

# in the example, at line y=10, there are 26 positions where a beacon cannot exist
# how many positions in the line y=2,000,000 cannot contain a beacon?

import re
from scipy.spatial.distance import cityblock

# collect the sensor and beacon locations from the input file
text = open("../data/15.txt").readlines()
data = []
regEx = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
for line in text:
  data.append(regEx.findall(line))
#print(data)

# we only care about y=2,000,000. Ignore any sensors that can't be in the y=2,000,000 range
ourY = 2000000
scannedX = set()
for sensor in data:
  sx, sy, bx, by = [int(coord) for coord in sensor[0]]
  radius = cityblock([sx, sy], [bx, by])
  ydist = abs(ourY-sy)
  # if it can't even theoretically reach our y, ignore it
  if radius < ydist:
    continue
  # if it can reach our y, add every possible x that it can reach
  else:
    for x in range(sx-(radius-ydist), sx+(radius-ydist)):
      scannedX.add(x)

# part 1 answer
print(len(scannedX))

####################### part 2 ##################
# now we care about the whole grid of 0<=x<=4000000 and 0<=y<=4000000 - 16 trillion squares! 
# instead of counting the "scanned" squares, we're finding the one "unscanned" square within these parameters
# conveniently, this lone "unscanned" square must, by definition, be next to the perimeter of at least 1 radius
# if we only look at these perimeters, we can reduce the number of operations from 16 trillion to something in the millions

# update, I tried the explanation above and collected 89,424,748 possible squares in just under 2 minutes. Still too slow

# I had to google this, but I can further reduce this 89mil by only checking the intersections of different radii (radiuses? idk)
# each "radius" can be thought of as 4 lines in the terms of y=mx+b. 
# Because it's a square grid, all of the lines are either parallel or perpendicular to one another
#  1.1.1.1
#  .1.1.1.
#  ..1X1..
#  .1.1.1.
#  1.1.1.1
# in the drawing above, if the 1s are the perimeters and the periods are the internals of two different scanners,
# then our solution has to be the X tile
# if 2 lines have the same slope, then we only care if the Y intercepts are within 2 of each other
# if they're perpendicular, then we have to find their intersection
# basically, unless they put the X on a perimeter tile (which is unlikely), this X has to live at the intersection of at least 2 scanners, probably 4

# intersections happen at (b-a)/2, (a+b)/2, where a is the positive slope (always +1) and b is the negative slope (always -1)

# positive slopes can be identified by being the connections between the top x left, and the bottom x right
# topY = sy - sx + radius + 1
# botY = sy - sx - radius - 1
# negative slopes can be identified by being the connections between the top x right, and the left x bottom
# topY = sx + sy + radius + 1
# botY = sx + sy - radius - 1

aSet = set()
bSet = set()
preSolvedSensors = []
for sensor in data:
  sx, sy, bx, by = [int(coord) for coord in sensor[0]]
  radius = cityblock([sx, sy], [bx, by])
  preSolvedSensors.append([sx, sy, radius])

  # add the positive slopes
  topY = sy - sx + radius + 1
  aSet.add(topY)
  botY = sy - sx - radius - 1
  aSet.add(botY)

  # add the negative slopes
  topY = sx + sy + radius + 1
  bSet.add(topY)
  botY = sx + sy - radius - 1
  bSet.add(botY)

# now we brute force these sets (there are only ~3000 permutations, don't worry)
# for every positive slope
for a in aSet:
  # for every negative slope
  for b in bSet:
    # build the intercepts
    xIntercept = (b-a)//2
    yIntercept = (a+b)//2
    # if it's outside of every radius
    if all(cityblock([xIntercept, yIntercept],[sensor[0], sensor[1]])>sensor[2] for sensor in preSolvedSensors):
      # and if it's in the plane
      if 0<xIntercept<=4000000 and 0<yIntercept<=4000000:
        # bingo - part 2 answer
        print(xIntercept*4000000+yIntercept)