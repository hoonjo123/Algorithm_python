#가로수

import math

N = int(input())

plantedTreesAreHere = []

for _ in range(N):
  plantedTreesAreHere.append(int(input()))

gap = []

for i in range(1, N):
  gap.append(plantedTreesAreHere[i]-plantedTreesAreHere[i-1])

#최대공약수만큼 간격을 두면.. 모든 가루수 간의 간격을 일정하게 할 수 있을듯..?
  
TreesGcd = gap[0]
for i in gap[1:]:
  TreesGcd = math.gcd(TreesGcd, i)

NeedTreesCounts = 0
for i in gap:
  NeedTreesCounts += (i // TreesGcd -1)

print(NeedTreesCounts)