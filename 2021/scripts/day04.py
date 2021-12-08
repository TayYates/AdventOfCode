import pandas as pd

items = []
pulls = [17,2,33,86,38,41,4,34,91,61,11,81,3,59,29,71,26,44,54,89,46,9,85,62,23,76,45,24,78,14,58,48,57,40,21,49,7,99,8,56,50,19,53,55,10,94,75,68,6,83,84,88,52,80,73,74,79,36,70,28,37,0,42,98,96,92,27,90,47,20,5,77,69,93,31,30,95,25,63,65,51,72,60,16,12,64,18,13,1,35,15,66,67,43,22,87,97,32,39,82]

with open('../data/day04.txt', 'r') as txt:
    for line in txt:
        items.append(line)

bingoCards = []

# build cards
for i in range(0, len(items), 6):
    # load data into a 5x5 dataframe
    data = [
        list(map(int, items[i].split())),
        list(map(int, items[i+1].split())),
        list(map(int, items[i+2].split())),
        list(map(int, items[i+3].split())),
        list(map(int, items[i+4].split())),
    ]
    df = pd.DataFrame(data, columns = ['0', '1', '2', '3', '4'])
    bingoCards.append(df)

# check for a bingo (max will be 50,000 if there are 5 10,000s in a row)
def checkCard(card):
    if max(card.sum(axis=1)) == 50000:
        return True
    elif max(card.sum(axis=0)) == 50000:
        return True

# for each pull, try each card
for pull in pulls:
    for bingoCard in bingoCards:
        # replace hits with 10,000
        bingoCard.replace(pull, 10000, inplace=True)
        # check if it won
        if checkCard(bingoCard):
            # answers are first and last values in this printout
            print(f"{(bingoCard.values.sum()%10000)*pull} on pull {pull}")
            # kill the card by setting values to -1 so that it can't win again
            bingoCard[bingoCard > -1] = -1