# from itertools import permutations

# N, M = map(int, input().split())

# for sequence in permutations(range(1, N + 1), M):
#     print(" ".join(map(str, sequence)))
def back(num):
  while len(num) == M:
    print(*num)
    break

  for i in range(1, N+1):
    if i not in num:
      back(num + [i])



N, M = map(int,(input().split()))
back([])