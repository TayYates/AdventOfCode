# part 1 

groups = open("../data/01-1.txt").read().split("\n\n")
#print(groups)

groupLists = [group.split("\n") for group in groups]
#print(groupLists)

sums = [sum(int(i) for i in group) for group in groupLists]
print(max(sums))

# part 2

sortedSums = sorted(sums)
print(sum(sortedSums[-3:]))