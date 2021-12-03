import math

items = []

with open('../data/day3.txt', 'r') as txt:
    for line in txt:
        items.append(line)

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

def partTwo(items, type):
    newItems, oldItems = [], items
    for i in range(0, 12):
        newGamma = buildAverages(oldItems)
        standard = math.floor(float((newGamma[i])/(len(oldItems)/2)))
        for item in oldItems:
            if type == 'positive':
                if int(item[i]) == standard:
                    newItems.append(item)
            else:
                if int(item[i]) != standard:
                    newItems.append(item)
        oldItems = newItems
        if len(newItems) == 1:
            return newItems[0]
        else:
            newItems = []

# gather answers from method
o = partTwo(items, 'positive')
c = partTwo(items, 'negative')
# remove \n and convert to decimal
o = int(o.strip("\n"), 2)
c = int(c.strip("\n"), 2)
# answer part 2
print(o * c)