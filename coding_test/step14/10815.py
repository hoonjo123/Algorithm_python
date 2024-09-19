#숫자 카드

import sys

input = sys.stdin.readline

N = int(input())

cards = set(map(int, input().split()))

M = int(input())

numbers = list(map(int, input().split()))


result = []
for num in numbers:
  if num in cards:
    result.append(1)
  else:
    result.append(0)

print(*result)