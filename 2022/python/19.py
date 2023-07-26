# which blueprint would maximize the number of geodes?
# quality level = id# * #geodesCracked@time=24
# part 1 answer is sum(quality levels)
import re

class Blueprint:
  def __init__(self, id, oreRobotCostOre, clayRobotCostOre, obsidianRobotCostOre, obsidianRobotCostClay, geodeRobotCostOre, geodeRobotCostObsidian):
    self.id = id
    self.oreRobotCostOre        = oreRobotCostOre
    self.clayRobotCostOre       = clayRobotCostOre
    self.obsidianRobotCostOre   = obsidianRobotCostOre
    self.obsidianRobotCostClay  = obsidianRobotCostClay
    self.geodeRobotCostOre      = geodeRobotCostOre
    self.geodeRobotCostObsidian = geodeRobotCostObsidian
    self.oreRobot      = 1
    self.clayRobot     = 0
    self.obsidianRobot = 0
    self.geodeRobot    = 0
    self.builtFlag     = False
    self.ore      = 0
    self.clay     = 0
    self.obsidian = 0
    self.geode    = 0
    # no reason to ever build more of a robot than you could possibly use
    self.oRlimit  = max(geodeRobotCostOre, obsidianRobotCostOre, clayRobotCostOre)
    self.cRlimit  = obsidianRobotCostClay
    self.obRlimit = geodeRobotCostObsidian

  def buildOreRobot(self):
    if self.ore>=self.oreRobotCostOre and self.oRlimit>self.oreRobot and self.builtFlag==False:
      self.ore      -= self.oreRobotCostOre
      self.oreRobot += 1
      self.builtFlag = True

  def buildClayRobot(self):
    if self.ore>=self.clayRobotCostOre and self.cRlimit>self.clayRobot and self.builtFlag==False:
      self.ore       -= self.clayRobotCostOre
      self.clayRobot += 1
      self.builtFlag  = True

  def buildObsidianRobot(self):
    if self.ore>=self.obsidianRobotCostOre and self.clay>=self.obsidianRobotCostClay and self.obRlimit>self.obsidianRobot and self.builtFlag==False:
      self.ore           -= self.obsidianRobotCostOre
      self.clay          -= self.obsidianRobotCostClay
      self.obsidianRobot += 1
      self.builtFlag      = True

  def buildGeodeRobot(self):
    if self.ore>=self.geodeRobotCostOre and self.obsidian>=self.geodeRobotCostObsidian and self.builtFlag==False:
      self.ore        -= self.geodeRobotCostOre
      self.obsidian   -= self.geodeRobotCostObsidian
      self.geodeRobot += 1
      self.builtFlag   = True

  def useRobots(self):
    return [self.oreRobot, self.clayRobot, self.obsidianRobot, self.geodeRobot]

  # I much prefer the problems that have a smart math solution, but this looks like it's just begging for a recusion loop. The only real choices here are DFS vs BFS
  def run(self, timeLimit):
    for _ in range(1, timeLimit):
      self.builtFlag = False
      # useRobots has to be called in the beginning, but it's additions can't be taken into account until the very end
      # this is because it takes 1 minute to mine the new resources, so they can't be available for use during the same minute that they were mined
      newResources = self.useRobots()
      self.buildGeodeRobot()
      self.buildObsidianRobot()
      self.buildClayRobot()
      self.buildOreRobot()
      self.ore += newResources[0]
      self.clay += newResources[1]
      self.obsidian += newResources[2]
      self.geode += newResources[3]


data = open("../data/19-sample.txt").read().split("\n")
regEx = re.compile(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.")

qualityLevel = 0
for line in data:
  print(line)
  match = regEx.match(line)
  bp = Blueprint(
    int(match.group(1)),
    int(match.group(2)),
    int(match.group(3)),
    int(match.group(4)),
    int(match.group(5)),
    int(match.group(6)),
    int(match.group(7))
  )
  bp.run(timeLimit=24)
  qualityLevel += int(match.group(1)) * bp.geode
  print(bp.geode)

# part 1 answer
print(qualityLevel)