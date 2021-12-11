from statistics import median

lines = []
with open('../data/day10.txt', 'r') as file:
    for line in file.read().splitlines():
        lines.append(line)

#####################################
# part 1

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

score = 0
for line in lines:
    # for each line, build a list called runners of all the openers currently in play
    runner = []
    for char in list(line):
        # if it's an opener, add it to runner
        if char in openers:
            runner.append(char)
        # when a closer appears, if the closer matches the most recent opener, annihilate that opener
        elif char in closers and char in closers[openers.index(runner[-1])]:
            runner.pop()
        else:
            # if the closer doesn't match the opener, add the score to the running total
            score += scores[char]
            break
# answer part 1
print(score)

#####################################
# part 2

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {'(': 1, '[': 2, '{': 3, '<': 4}

lineScores = []
for line in lines:
    badLine = False
    # for each line, build a list called runners of all the openers currently in play
    score = 0
    runner = []
    for char in list(line):
        # build counts of all items
        if char in openers:
            # add opener to runner
            runner.append(char)
        # when a closer appears, if the closer matches the most recent opener, annihilate that opener
        elif char in closers and char in closers[openers.index(runner[-1])]:
            runner.pop()
        # else, this is a corrupted line, don't count the score here
        else:
            badLine = True
            break
    # run through the runner list, popping items and adding to the score until you've run through them all
    while len(runner) > 0:
        score *= 5
        score += scores[runner[-1]]
        runner.pop()
    # only append non corrupted lines
    if badLine == False:
        lineScores.append(score)
# answer part 2
print(median(lineScores))