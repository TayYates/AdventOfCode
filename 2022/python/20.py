from collections import deque

def run(times, key):
  
  ogList = [int(i)*key for i in open("../data/20.txt").read().split("\n")]
  deck = deque(ogList)

  for _ in range(times):
    # this is our main loop. We need to modify deck once for each item in ogList
    for i in ogList:
      # find i in deck
      index = deck.index(i)
      # ok I want to try something cool here, deque allows us to spin the list around instead of trying to deal with insertions
      # spin your number to the front, pop it, spin the direction and distance it moves, place it, and then return to where you came from
      deck.rotate(-index)
      deck.popleft()
      deck.rotate(-i)
      deck.appendleft(i)
      # the extra +1 is to account for the implicit -1 that comes from popleft()
      deck.rotate(i+index+1)

  ans = 0
  # rotate the deck so that zero is at the beginning
  deck.rotate(-deck.index(0))
  for _ in range(3):
    deck.rotate(-1000)
    ans += deck[0]
  return ans

print(run(1, 1))
print(run(10, 811589153))