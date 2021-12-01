depths = []
with open('../data/day1.txt', 'r') as txt:
    for line in txt:
        depths.append(int(line))

print(sum(a < b for a, b in zip(depths, depths[1:])))
print(sum(a < b for a, b in zip(depths, depths[3:])))