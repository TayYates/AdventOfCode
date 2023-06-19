groups = open("../data/01-1.txt").read().split("\n\n")
#print(groups)

groupLists = [group.split("\n") for group in groups]
#print(groupLists)

sums = [sum(int(i) for i in group) for group in groupLists]
# part 1 answer
print(max(sums))

sortedSums = sorted(sums)
# part 2 answer
print(sum(sortedSums[-3:]))