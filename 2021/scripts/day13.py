import numpy as np

#########################
# data prep

dots = []
folds = []
maxX, maxY = 0, 0

with open('../data/day13.txt', 'r') as file:
    for line in file.read().splitlines():
        if 'fold' in line:
            # format - [axis, location]
            fold = list(line.split(" ")[-1].split("="))
            folds.append(fold)
        elif line:
            # format - [x, y]
            x = int(line.split(",")[0])
            y = int(line.split(",")[1])
            # use these to build the numpy array, rather than finding the max of the fully built tuple
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
            dots.append(tuple([x, y]))

# build a numpy array of zeros, and fill the dots into the array
dotMap = np.zeros((maxX + 1, maxY + 1))
for dot in dots:
    dotMap[dot] = 1


#########################
# part 1

def folder(dotMap, fold):
    direction, location = fold[0], int(fold[1])
    # fold horizontally if x, vertically if y
    if direction == 'x':
        # take the section and flip it
        flippedSection = dotMap[(location+1):,:]
        flippedSection = np.flipud(flippedSection)
        # add that selection back on the mirrored image
        dotMap[(2*location - len(dotMap)+1):location,:] += flippedSection
        dotMap = dotMap[:location,:]
    elif direction == 'y':
        # take the section and flip it
        flippedSection = dotMap[:,(location+1):]
        flippedSection = np.fliplr(flippedSection)
        # add that selection back on the mirrored image
        dotMap[:,(2*location-len(dotMap[0])+1):location] += flippedSection
        dotMap = dotMap[:,:location]

    return dotMap

# only run the first fold
dotMap = folder(dotMap, folds[0])
# answer part 1
print(np.count_nonzero(dotMap))

#########################
# part 2

# iterate through each fold
for fold in folds:
    dotMap = folder(dotMap, fold)
dotMap[dotMap > 0] = '99'
# answer part 2
# If you find it hard to read the letters, you can replace '99' with '#' and '0' with ''
print(dotMap)