import math
items = []

with open('../data/day3.txt', 'r') as txt:
    for line in txt:
        items.append(line)

# begin part 1
def buildAverages(items):
    digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for item in items:
        for i in range(0, len(item)-1):
            digits[i] += int(item[i])
    return digits

gamma, epsilon = '', ''
digits = buildAverages(items)
for i in range(0, len(digits)):
    if digits[i] > 500:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'

# answer part 1
print(int(gamma, 2) * int(epsilon, 2))

# begin part 2
def partTwo(items, type):
    newItems, oldItems = [], items
    for i in range(0, 12):
        # recalculate the most common value and name it 'standard'
        newGamma = buildAverages(oldItems)
        standard = math.floor(float((newGamma[i])/(len(oldItems)/2)))
        # go through each remaining item, checking against standard
        for item in oldItems:
            # if oxygen, conform to standard, if co2 go against standard
            if type == 'oxygen':
                if int(item[i]) == standard:
                    newItems.append(item)
            else:
                if int(item[i]) != standard:
                    newItems.append(item)
        # use newItems as the oldItems for the next iteration
        oldItems = newItems
        # if only one left, return answer
        if len(newItems) == 1:
            return newItems[0].strip("\n")
        # else, continue iterating
        else:
            newItems = []

# run the partTwo method and convert binary to decimal
o = int(partTwo(items, 'oxygen'), 2)
c = int(partTwo(items, 'co2'), 2)

# answer part 2
print(o * c)