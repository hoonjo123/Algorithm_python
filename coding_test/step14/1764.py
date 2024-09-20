#듣보잡
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

neverHeardSet = set(input().strip() for _ in range(N))
neverSeenSet = set(input().strip() for _ in range(M))

neverHeardAndSeen = sorted(neverHeardSet & neverSeenSet)

print(len(neverHeardAndSeen))
for name in neverHeardAndSeen:
  print(name)