data = open("../data/13.txt").read().split("\n\n")
# easier to build a dict than to keep track of index locations by hand
pairs = {i: (eval(p[0]), eval(p[1])) for i, p in enumerate([p.splitlines() for p in data], 1)}
#print(pairs)

def compare(left, right):
  for l, r in zip(left, right):
    if isinstance(l, int) and isinstance(r, int):
      if l < r: return True
      if l > r: return False
    elif isinstance(l, list) and isinstance(r, list):
      result = compare(l, r)
      if result != None: return result
    elif isinstance(l, int):
      result = compare([l], r)
      if result != None: return result
    else:
      result = compare(l, [r])
      if result != None: return result
    
  if len(left) < len(right): return True
  elif len(left) > len(right): return False
  else: return None

rightOrd = 0
for k, v in pairs.items():
  if compare(v[0], v[1]):
    rightOrd += k
# part 1 answer
print(rightOrd)

all_pairs = [a for b in list(pairs.values()) for a in b]
all_pairs.append([[[2]], [[6]]])

compare2 = 1 + sum(1 for p in all_pairs if compare(p, [[2]]))
compare6 = 1 + sum(1 for p in all_pairs if compare(p, [[6]]))
# part 2 answer
print(compare2*compare6)