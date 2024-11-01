# 붙임성 좋은 총총이
N = int(input())
dancerSet = {"ChongChong"}

for _ in range(N):
  A, B = input().split()
  if A in dancerSet or B in dancerSet:
    dancerSet.add(A)
    dancerSet.add(B)

print(len(dancerSet))