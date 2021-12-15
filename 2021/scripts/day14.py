#########################
# data prep

oldPolymer = []
newPolymer = []
formulas = {}
polymerCounts = {}

with open('../data/day14.txt', 'r') as file:
    for line in file.read().splitlines():
        if line:
            if '->' in line:
                items = line.split(" -> ")
                formulas[items[0]] = items[1]
                polymerCounts[items[1]] = 0
            else:
                ogPolymer = list(line.strip('\n'))
            # I know this isn't clean but I need the original polymer for part 2 from before part 1 extended it
            oldPolymer = ogPolymer

#########################
# part 1 - brute force

def synthesize(oldPolymer, formulas, polymerCounts):
    polymerCounts[oldPolymer[0]] += 1
    newPolymer = [oldPolymer[0]]
    newLetter = oldPolymer[0]
    for j in range(1, len(oldPolymer)):
        # retrieve the instructions for this run
        instructions = oldPolymer[j-1] + oldPolymer[j]
        # create the new letter using the formulas dictionary
        newLetter = formulas[instructions]
        # count the letter added towards the running sum for each letter
        polymerCounts[newLetter] += 1
        # append both letters used to the new polymer
        newPolymer.append(newLetter)
        newPolymer.append(oldPolymer[j])
    return newPolymer, polymerCounts

# run the self replicating polymer (cough, definitely not RNA replication, cough) 10 times
for i in range(0, 10):
    print(i)
    newPolymer, polymerCounts = synthesize(oldPolymer, formulas, polymerCounts)
    oldPolymer = newPolymer
# answer part 1
print(polymerCounts)

#########################
# part 2 - efficient

# build empty dict of all pairs
oldPairCounts = {}
for formula in formulas:
    oldPairCounts[formula] = 0

# kickstart the dictionary with the initial string
for j in range(1, len(ogPolymer)):
    pair = ogPolymer[j-1] + ogPolymer[j]
    oldPairCounts[pair] += 1

# simulates polymer generation by counting the pairs that would have been created
def buildDict(oldPairCounts, formulas):
    newPairCounts = {}
    for pair in oldPairCounts:
        # establish the number of pairs, and the letter they will create
        oldCount = oldPairCounts[pair]
        newLetter = formulas[pair]
        # add oldCount to the new pairs this new letter will create
        newPairCounts[pair[0] + newLetter] = newPairCounts.get(pair[0] + newLetter, 0) + oldCount
        newPairCounts[newLetter + pair[1]] = newPairCounts.get(newLetter + pair[1], 0) + oldCount
    return newPairCounts

# run buildDict the appropriate number of time to build a dictionary of pair counts
for i in range(0, 40):
    newPairCounts = buildDict(oldPairCounts, formulas)
    oldPairCounts = newPairCounts

# translate these pair counts into letter counts
polymerCounts = {x:0 for x in polymerCounts}
for pair in newPairCounts:
    polymerCounts[formulas[pair]] += newPairCounts.get(pair, 0)
# answer 2
print(max(polymerCounts.values()) - min(polymerCounts.values()))