#대칭 차집합

#대칭 차집합? (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합

import sys
input = sys.stdin.readline
# N, M = map(int,(input().split()))

# A = set(map(int,input().split()))
# B = set(map(int,input().split()))

# difference = A.difference(B)


# print(len(difference))


N, M = map(int,input().split())

A = set()
for _ in range(N):
  A.add(int(input()))

B = set()
for _ in range(M):
  B.add(int(input()))

symmetric_difference = A.symmetric_difference(B)

print(len(symmetric_difference))



# a = {1, 2, 3}
# b = {3, 4, 5}
# # 대칭 차집합
# print(a.symmetric_difference(b))  # 또는 a ^ b

# # 합집합
# print(a.union(b))  # 또는 a | b

# # 교집합
# print(a.intersection(b))  # 또는 a & b

# # 차집합
# print(a.difference(b))  # 또는 a - b