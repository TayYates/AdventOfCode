text = open("../data/06-1.txt").read()

ans1, ans2 = False, False
for i in range(len(text)):
  if len(set(text[i:i+4])) == 4 and not ans1:
    # part 1 answer
    ans1 = i+4
  if len(set(text[i:i+14])) == 14 and not ans2:
    # part 2 answer
    ans2 = i+14
print(ans1, ans2)