data = open("../data/04-1.txt").read().split("\n")

def findOverlap(myPair, part):
  first, second = myPair[0].split('-'), myPair[1].split('-')
  if part == '1':
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]) or int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
      return 1
  elif part == '2':
    if (int(first[0]) >= int(second[0]) and int(second[1]) >= int(first[0])) or (int(second[0]) >= int(first[0]) and int(second[0]) <= int(first[1])):
      return 1
  return 0

count1, count2 = 0, 0
for line in data:
  myPair = line.split(",")
  count1 += findOverlap(myPair, '1')
  count2 += findOverlap(myPair, '2')

# part 1 answer
print(count1)
# part 2 answer
print(count2)