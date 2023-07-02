import re
from copy import deepcopy

movesText = open("../data/05-moves.txt").read().split("\n")

moveRe = re.compile(r"move (\d+) from (\d+) to (\d+)")
moves = [re.findall(moveRe, move)[0] for move in movesText]
#print(moves) # this is a list of tuples

def part1(stacks, moves):
  for move in moves:
    for _ in range(int(move[0])):
      stacks[int(move[2])-1].append(stacks[int(move[1])-1].pop())
  return stacks

def part2(stacks, moves):
  for move in moves:
    stacks[int(move[2])-1] += stacks[int(move[1])-1][-int(move[0]):]
    stacks[int(move[1])-1] = stacks[int(move[1])-1][:-int(move[0])]
  return stacks

# initialize the stacks, and fill them with the crates at time zero
"""
I found the easiest way to do this was to remove the legend from the source data 
and replace whitespace with '_'. After you do this, you can reverse the list 
and it will be in the right order.
"""
stacks = [[] for _ in range(9)]
cratesText = open("../data/05-crates.txt").read().replace(" ", "_").split("\n")
cratesText.reverse()
# not pythonic, but it gets the job done :shrug:
for line in cratesText:
  for i in range(1, len(line), 4):
    crate = line[i]
    if crate != "_":
      stacks[i//4].append(crate)
#print(stacks)
"""
deepcopy is necessary because otherwise the list of lists will 
not be a true copy, they'll both reference the same 
space in memory and overwrite one another
"""
p1Stacks = deepcopy(stacks)
p2Stacks = deepcopy(stacks)

endState1 = part1(p1Stacks, moves)
endState2 = part2(p2Stacks, moves)

# initial state
print("".join([stack[-1] for stack in stacks]))
# part 1 answer
print("".join([stack[-1] for stack in endState1]))
# part 2 answer
print("".join([stack[-1] for stack in endState2]))
