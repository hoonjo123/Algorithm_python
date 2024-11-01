#인사성 밝은 곰곰이(귀여웡)

N = int(input())
count = 0
users = set()

for _ in range(N):
  newperson = input().strip()
  if newperson == "ENTER":
    users.clear()
  else:
    if newperson not in users:
      count += 1
      users.add(newperson)


print(count)