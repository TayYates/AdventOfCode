import numpy as np
import re

def runTest(part):
    # build 1,000 x 1,000 array of 0s
    seaFloor = np.zeros((1000,1000), dtype=int)

    # transform each line into a list of points, store these in commands
    commands = []
    with open('../data/day5.txt', 'r') as txt:
        for line in txt:
            line = re.split(',| -> ', line.strip())
            command = [
                int(line[0]),
                int(line[1]),
                int(line[2]),
                int(line[3]),
            ]
            commands.append(command)

    for command in commands:
        # for each command list, establish min and max for X and Y
        Xmin, Ymin, Xmax, Ymax = min(command[0], command[2]), min(command[1], command[3]), max(command[0], command[2]), max(command[1], command[3])
        # if Y is constant
        if Ymin == Ymax:
            # +1 onto grid from Xmin to Xmax
            seaFloor[Ymin, Xmin:(Xmax+1)] += 1
        # if X is constant
        elif Xmin == Xmax:
            # +1 onto grid from Ymin to Ymax
            seaFloor[Ymin:(Ymax+1), Xmin] += 1
        # if diagonal. Only run for part2
        elif part == 'part 2':
            # build variables for magnitude and direction
            deltaX = command[2] - command[0]
            deltaY = command[3] - command[1]
            Xdirection = deltaX / abs(deltaX)
            Ydirection = deltaY / abs(deltaY)
            # give this for loop a starting place, a magnitude, and a direction and let it add 1 to each point
            for i in range(0, max(abs(deltaX), abs(deltaY)) + 1):
                Yposition = int(command[1] + (i * Ydirection))
                Xposition = int(command[0] + (i * Xdirection))
                seaFloor[Yposition][Xposition] += 1

    # answer
    print(np.count_nonzero(seaFloor > 1))

runTest('part 1')
runTest('part 2')