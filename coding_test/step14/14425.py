#문자열 집합
import sys

input = sys.stdin.readline

N, M = map(int, input().split())


S = set()
for _ in range(N):
  S.add(input().strip())


count = 0
for _ in range(M):
  if input().strip() in S:
    count += 1

print(count)
