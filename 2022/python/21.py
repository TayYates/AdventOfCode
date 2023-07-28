from copy import deepcopy

m = {}

for input in open("../data/21.txt").read().split("\n"):
  mList = input.split()
  if len(mList) == 4:
    m[mList[0][:-1]] = {
      "op": mList[2],
      "left": mList[1],
      "right": mList[3],
      "value": None,
      "done": False
    }
  elif len(mList) == 2:
    m[mList[0][:-1]] = {
      "op": None,
      "value": int(mList[1]),
      "done": False
    }


def run(m):
  numMonkeys = len(m)
  numDone = 0

  while numDone < numMonkeys:
    for monkey in m:
      if m[monkey]["done"] == False:

        if m[monkey]["op"] == "+":
          l, r = m[monkey]["left"], m[monkey]["right"]
          if m[l]["done"] == True and m[r]["done"] == True:
            m[monkey]["value"] = m[l]["value"] + m[r]["value"]
            m[monkey]["done"] = True

        elif m[monkey]["op"] == "-":
          l, r = m[monkey]["left"], m[monkey]["right"]
          if m[l]["done"] == True and m[r]["done"] == True:
            m[monkey]["value"] = m[l]["value"] - m[r]["value"]
            m[monkey]["done"] = True

        elif m[monkey]["op"] == "*":
          l, r = m[monkey]["left"], m[monkey]["right"]
          if m[l]["done"] == True and m[r]["done"] == True:
            m[monkey]["value"] = m[l]["value"] * m[r]["value"]
            m[monkey]["done"] = True

        elif m[monkey]["op"] == "/":
          l, r = m[monkey]["left"], m[monkey]["right"]
          if m[l]["done"] == True and m[r]["done"] == True:
            m[monkey]["value"] = m[l]["value"] / m[r]["value"]
            m[monkey]["done"] = True

        else:
          m[monkey]["done"] = True

        if m[monkey]["done"] == True:
          numDone += 1

  return m

mStatic = deepcopy(m)
m1 = run(m)
# part 1 answer
print(m1["root"]["value"])

########################## part 2 #########################

# part 1 only took 78 milliseconds, and I tried to brute force this but I could tell I was getting nowhere when I passed 10,000
# instead, I printed the difference between l and r and goal searched it to zero, BY HAND
# at 13 digits and approx 2-3 adjustments per digit, this took approximately 2-3 minutes of real world time

# make the necessary adjustments
m = deepcopy(mStatic)
i = 3220993874133
m["humn"]["value"] = i
m1 = run(m)
l, r = m1["root"]["left"], m1["root"]["right"]
print(m1[l]["value"] - m1[r]["value"])

# part 2 answer
print(i)