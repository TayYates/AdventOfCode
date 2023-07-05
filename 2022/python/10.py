import sys

screen = ['.' for _ in range(240)]

commands = open("../data/10.txt").read().splitlines()

strengths = [1]
signal = 1

for command in commands:
  if abs(signal%40 - (len(strengths)-1)%40) <= 1:
    screen[len(strengths)-1] = '#'
  strengths.append(signal*len(strengths))
  
  if "add" in command:
    if abs(signal%40 - (len(strengths)-1)%40) <= 1:
      screen[len(strengths)-1] = '#'
    strengths.append(signal*len(strengths))
    signal += int(command.split()[1])

ans1 = strengths[20] + strengths[60] + strengths[100] + strengths[140] + strengths[180] + strengths[220]
# part 1 answer
print(ans1)

# part 2 answer
for i in range(240):
  if i%40 == 0:
    print()
  sys.stdout.write(str(screen[i]))