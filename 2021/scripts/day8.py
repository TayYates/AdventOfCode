# 10 unique patterns, 0-9
items = []
with open('../data/day8.txt', 'r') as txt:
    for line in txt:
        items.append(line)


#######################
# part 1
digitCounter = 0
# brute force, sum all strings that aren't 5 or 6 characters long
for item in items:
    lineList = item.strip("\n").split("|")
    outputs = lineList[1].split(" ")[1:]
    for output in outputs:
        if len(output) != 5 and len(output) != 6:
            digitCounter += 1
# part 1 answer
print(digitCounter)

#######################
# part 2

# counts number of identical chars in two strings, agnostic of their positions
def intersect(i, masterKey):
    value = 0
    for char in i:
        if char in masterKey:
            value += 1
    return value

# ladder logic, but in Python,,,,
def buildDigits(input, output):
    digits = ''
    # have to parse these two from input as well as output just to make sure we find them at least once
    # they're used to differentiate between the strings with a length of 5 or 6
    for i in input:
        if len(i) == 2:
            one = i
        elif len(i) == 4:
            four = i
    # establish the answer for each len(i) using basic logic
    for i in output:
        if len(i) == 2:
            digits += '1'

        elif len(i) == 3:
            digits += '7'

        elif len(i) == 4:
            digits += '4'

        # len(5) and len(6) require a conditional based on how '1' and '4' are wired
        elif len(i) == 5:
            if intersect(i,one) == 2:
                digits += '3'
            elif intersect(i,four) == 2:
                digits += '2'
            else:
                digits += '5'

        elif len(i) == 6:
            if intersect(i,four) == 4:
                digits += '9'
            elif intersect(i,one) == 2:
                digits += '0'
            else:
                digits += '6'

        # back to simple logic :)
        elif len(i) == 7:
            digits += '8'

    # return the 4 digit string
    return digits

# part 2 driver script
finalAnswer = []
for item in items:
    # split up inputs and outputs and clean the input data
    lineList = item.strip("\n").split(" | ")
    input, output = lineList[0].split(" "), lineList[1].split(" ")
    # pass each item into the logic method
    digits = buildDigits(input, output)
    # convert the item answer to an integer and append it to the final answer list
    finalAnswer.append(int(digits))
# answer 2
print(sum(finalAnswer))