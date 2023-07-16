# wind speeds per time. Very important to use .strip()! I beat my head against a wall for a while because "\n" was a hidden input for wind[i]
wind = open("../data/17.txt").read().strip()
windLen = len(wind)

shapes = {
  0: set([(2,0), (3,0), (4,0), (5,0)]),
  1: set([(3,2), (2,1), (3,1), (4,1), (3,0)]),
  2: set([(2,0), (3,0), (4,0), (4,1), (4,2)]),
  3: set([(2,0), (2,1), (2,2), (2,3)]),
  4: set([(2,1), (2,0), (3,1), (3,0)]),
}

# this will be adjusted for the height of the tetris situation later. Default to y=0
floorRow = set([(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0)])

def moveShape(direction, piece):
  # move left, ignore if already on wall
  if direction == "left":
    if any([x==0 for (x,y) in piece]):
      return piece
    return set([(x-1,y) for (x,y) in piece])
  # move right, ignore if already on wall
  elif direction == "right":
    if any([x==6 for (x,y) in piece]):
      return piece
    return set([(x+1,y) for (x,y) in piece])
  # move down
  elif direction == "down":
    return set([(x,y-1) for (x,y) in piece])
  # move up
  elif direction == "up":
    return set([(x,y+1) for (x,y) in piece])

# needed this for part 2. Basically, it's a snapshot of the situation so that we can find a pattern
def pattern(row):
  maxY = max([y for (x,y) in row])
  # this had to be a frozenset because it won't let me hash a normal set
  pattern = frozenset([(x,maxY-y) for (x,y) in row if maxY-y<=30])
  return pattern

timeElapsed = 0
maxHeight = 0
uniques = {}
added = 0
i = 0
maxTime = 1_000_000_000_000

while timeElapsed < maxTime:
  shape = set([(x, y + maxHeight + 4) for (x, y) in shapes[timeElapsed%5]])
  
  # yes I know, not perfect, but it has an iterator hidden in the whileTrue statement with a guaranteed exit
  while True:
    # do your movements
    if wind[i] == '<':
      shape = moveShape("left", shape)
      if shape & floorRow:
        shape = moveShape("right", shape)
    else:
      shape = moveShape("right", shape)
      if shape & floorRow:
        shape = moveShape("left", shape)
    # the wind input needs to endlessly cycle, so we exploit the modulo
    i = (i+1)%windLen
    shape = moveShape("down", shape)
    if shape & floorRow:
      shape = moveShape("up", shape)
      floorRow |= shape
      maxHeight = max([y for (_,y) in floorRow])

      # part 2 pattern recognition
      SR = (i, timeElapsed%5, pattern(floorRow))
      # got it, finally, a repeat offender. Noe we can jump by this deltaY instead of by 1
      if SR in uniques and timeElapsed>=2022:
        (oldTime, oldY) = uniques[SR]
        changeY = maxHeight - oldY
        # If this number were 100, this would be 100x more efficient than brute force, etc etc
        changeTime = timeElapsed - oldTime
        amt = (maxTime - timeElapsed)//changeTime
        added += amt * changeY
        timeElapsed += changeTime*amt
        # break the first loop that went over the time limit
        assert timeElapsed < maxTime
      uniques[SR] = (timeElapsed, maxHeight)
      print(len(uniques))
      break
  timeElapsed += 1
  # part 1 answer
  if timeElapsed == 2022:
    print(maxHeight+added)
# part 2 answer
print(maxHeight+added)