runs = open("../data/02-1.txt").read().split("\n")

winners = ['A Y', 'B Z', 'C X']
losers = ['A Z', 'B X', 'C Y']
draws = ['A X', 'B Y', 'C Z']

score = 0
for run in runs:
    if run in winners:
        score += 6
    elif run in draws:
        score += 3

    if 'X' in run:
        score += 1
    elif 'Y' in run:
        score += 2
    elif 'Z' in run:
        score += 3

# part 1 answer
print(score)

# no need to get fancy here, only 9 permutations
score = 0
scoreDict = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}
for run in runs:
    score += scoreDict[run]
# part 2 answer
print(score)