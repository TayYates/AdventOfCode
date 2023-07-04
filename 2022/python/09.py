import numpy as np

moves = open("../data/09.txt").read().splitlines()
#print(moves)

def headMove(head, direction):
  if direction == 'U':
      head[1] += 1
  elif direction == 'D':
    head[1] -= 1
  elif direction == 'L':
    head[0] -= 1
  elif direction == 'R':
    head[0] += 1
  return head

def tailMove(head, tail):
  if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
    if head[0] > tail[0]:
      tail[0] += 1
    elif head[0] < tail[0]:
      tail[0] -= 1
    if head[1] > tail[1]:
      tail[1] += 1
    elif head[1] < tail[1]:
      tail[1] -= 1
  return tail

# keep current locations of head and tail, and maintain a set of where the tail has been
head = np.array([0,0])
tail = np.array([0,0])
history = set()
history2 = set()

for move in moves:
  direction, distance = move.split()[0], int(move.split()[1])
  # move the head one step at a time
  for d in range(0, distance):
    # move the head
    head = headMove(head, direction)
    # move the tail in response
    tail = tailMove(head, tail)
    # update history
    history.add(tuple(tail))

# part 1 answer - this assumes that 0,0 is visited a second time, because we never accounted for it in the beginning
print(len(history))

############ doing part 2 separate because it would be messy to do it all at once

# need 10 tails, where rope[i+1] treats rope[i] as the head
rope = np.array([[0,0] for _ in range(10)])

for move in moves:
  direction, distance = move.split()[0], int(move.split()[1])
  # move the head one step at a time
  for d in range(0, distance):
    # move the head
    rope[0] = headMove(rope[0], direction)
    # move the tail in response
    for i in range(1, len(rope)):
      rope[i] = tailMove(rope[i-1], rope[i])
    # update history
    history2.add(tuple(rope[-1]))

# part 2 answer - also assumes that 0,0 is visited a second time
print(len(history2))