import sys

screen = ['.' for _ in range(240)]

commands = open("../data/10.txt").read().splitlines()

strengths = [1]
signal = 1

for command in commands:
  clock = len(strengths)
  if abs(signal%40 - (clock-1)%40) <= 1:
    screen[clock-1] = '#'
  strengths.append(signal*clock)
  
  if "add" in command:
    clock = len(strengths)
    if abs(signal%40 - (clock-1)%40) <= 1:
      screen[clock-1] = '#'
    strengths.append(signal*clock)
    signal += int(command.split()[1])

ans1 = strengths[20] + strengths[60] + strengths[100] + strengths[140] + strengths[180] + strengths[220]
# part 1 answer
print(ans1)

# part 2 answer
for i in range(240):
  if i%40 == 0:
    print()
  sys.stdout.write(str(screen[i]))