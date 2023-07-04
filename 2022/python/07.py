text = open("../data/07-1.txt").read().split("\n")

# simulate a directory structure with a list
currDir = ["root"]
dirsDict = {currDir[0]: 0}
for line in text:
  if "$ cd " in line:
    if ".." in line:
      currDir = currDir[:-1]
    elif "/" not in line:
      # this is the only condition where we add a directory
      currDir.append(line.split(" ")[-1])
      dirsDict["/".join(currDir)] = 0
  elif "dir " not in line and "$ ls" not in line:
    # when you add a filesize, you have to do it recursively
    for i in range(1, len(currDir)+1):
      dirsDict["/".join(currDir[:i])] += int(line.split(" ")[0])

# part 1 answer
print(sum([v for v in dirsDict.values() if v <= 100000]))
# part 2 answer
print(min([v for v in dirsDict.values() if v >= 30000000 - (70000000 - dirsDict["root"])]))