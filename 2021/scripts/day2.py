items, direction, magnitude = [], [], []
horiz, depth1, depth2, aim = 0, 0, 0, 0
with open('../data/day2.txt', 'r') as txt:
    for line in txt:
        line = line.strip("\n")
        direction.append(line.split(" ")[0])
        magnitude.append(int(line.split(" ")[1]))

for (dir, mag) in zip(direction, magnitude):
    if dir == "forward":
        horiz += mag
        depth2 += mag * aim
    elif dir == "down":
        depth1 += mag
        aim += mag
    else:
        depth1 -= mag
        aim -= mag

# answer part 1
print(horiz * depth1)
# answer part 2
print(horiz * depth2)