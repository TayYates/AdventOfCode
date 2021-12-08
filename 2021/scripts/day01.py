depths = []
with open('../data/day01.txt', 'r') as txt:
    for line in txt:
        depths.append(int(line))

# answer part 1
print(sum(a < b for a, b in zip(depths, depths[1:])))
# answer part 2
print(sum(a < b for a, b in zip(depths, depths[3:])))