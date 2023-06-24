data = open("../data/03-1.txt").read().split("\n")

def findDouble(myLine):
  half, rem = divmod(len(myLine), 2)
  first, second = myLine[:half], myLine[half:]
  for char in first:
    if char in second:
      return char

def findTriple(myLines):
  for char in myLines[0]:
    if char in myLines[1] and char in myLines[2]:
      return char

def findValue(myChar):
  val = ord(myChar)
  if val >= 97:
    return val - 96
  else:
    return val - 38

sumValues = 0

for line in data:
  myDouble = findDouble(line)
  sumValues += findValue(myDouble)

# part 1 answer
print(sumValues)

sumValues = 0

for _ in range(0, len(data), 3):
  myLines = data[_:_+3]
  myTriple = findTriple(myLines)
  sumValues += findValue(myTriple)

# part 2 answer
print(sumValues)