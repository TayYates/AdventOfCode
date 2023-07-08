import re
from math import prod

text = open("../data/11.txt").read().split("\n\n")

# this is our monkey schema
monkeys = {i: {
  "items":  [], # list
  "ops":    [], # list
  "divBy":  [], # int
  "tThrow": [], # int
  "fThrow": [], # int
  "score":   0  # int
} for i in range(len(text))}

# build the initial state using regex
reTest = re.compile('Monkey (\d+):\n  Starting items: ([0-9, ]+)\n  Operation: new = old (. \d+|. \w+)\n  Test:'
                    ' divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)')
for item in text:
  m = list(re.findall(reTest, item)[0])
  index = int(m[0])
  monkeys[index]["items"]  = [int(v) for v in m[1].split(", ")]
  monkeys[index]["ops"]    = m[2].split()
  monkeys[index]["divBy"]  = int(m[3])
  monkeys[index]["tThrow"] = int(m[4])
  monkeys[index]["fThrow"] = int(m[5])
  #print(monkeys[index].values())

for _ in range(20):
  for monkey in monkeys.values():
    if len(monkey["items"]) < 1: continue
    # monkey inspects item, adding to worry
    for item in monkey["items"]:
      if monkey["ops"][1] == 'old':
          item *= item
      elif monkey["ops"][0] == '+':
        item += int(monkey["ops"][1])
      else: 
        item *= int(monkey["ops"][1])
      # after inspection but before test, worry is divided by 3 and the remainder is discarded
      item //= 3
      # monkey throws the item
      if item % monkey["divBy"] == 0:
        monkeys[monkey["tThrow"]]["items"].append(item)
      else:
        monkeys[monkey["fThrow"]]["items"].append(item)
      monkey["score"] += 1
      monkey["items"] = monkey["items"][1:]

#print(monkeys.values())
scores = [m["score"] for m in monkeys.values()]
scores.sort()
# part 1 answer
print(scores[-1]*scores[-2])

#############################################################################
# part 2 complicates things because all the integers get way too big, we need to 
# shrink the numbers somehow in a way that doesn't change the answer in the end

# for cleanliness, I've copy/pasted the whole operation so that both part1 and part2 run without any modifications
for item in text:
  m = list(re.findall(reTest, item)[0])
  index = int(m[0])
  monkeys[index]["items"]  = [int(v) for v in m[1].split(", ")]
  monkeys[index]["ops"]    = m[2].split()
  monkeys[index]["divBy"]  = int(m[3])
  monkeys[index]["tThrow"] = int(m[4])
  monkeys[index]["fThrow"] = int(m[5])
  monkeys[index]["score"]  = 0
  #print(monkeys[index].values())

# build the least common denominator between all 8 monkeys' test numbers
# probably not the *least* common denominator, but it gets the runtime down to less than 1 second so that's good enough
divBys = [monkey["divBy"] for monkey in monkeys.values()]
#print(prod(divBys))

for _ in range(10000):
  for monkey in monkeys.values():
    if len(monkey["items"]) < 1: continue
    # monkey inspects item, adding to worry
    for item in monkey["items"]:
      if monkey["ops"][1] == 'old':
          item *= item
      elif monkey["ops"][0] == '+':
        item += int(monkey["ops"][1])
      else: 
        item *= int(monkey["ops"][1])

      # the secret sauce for part 2, it shrinks the numbers in a way that doesn't change the answers
      # because any value higher than prod(divBys) would be ignored by the test on line 93 anyway
      item %= prod(divBys)

      # monkey throws the item
      if item % monkey["divBy"] == 0:
        monkeys[monkey["tThrow"]]["items"].append(item)
      else:
        monkeys[monkey["fThrow"]]["items"].append(item)
      monkey["score"] += 1
      monkey["items"] = monkey["items"][1:]

#print(monkeys.values())
scores = [m["score"] for m in monkeys.values()]
scores.sort()
# part 2 answer
print(scores[-1]*scores[-2])