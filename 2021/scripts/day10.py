from statistics import median

lines = []
with open('../data/day10.txt', 'r') as file:
    for line in file.read().splitlines():
        lines.append(line)

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {'(': 1, '[': 2, '{': 3, '<': 4}

score1 = 0
lineScores = []
for line in lines:
    badLine = False
    score2 = 0
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
            score1 += scores1[char]
            badLine = True
            break
    if badLine == False:
        # go through the runner list, popping items and adding to the score until you've run through them all
        while len(runner) > 0:
            score2 *= 5
            score2 += scores2[runner[-1]]
            runner.pop()
        lineScores.append(score2)
# answer part 1
print(score1)
# answer part 2
print(median(lineScores))