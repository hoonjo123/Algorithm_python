#수 정렬하기
N = int(input())

num = []
for _ in range(N):
  num.append(int(input()))


# b = sorted(set(num))
# print(b)
num.sort()

for i in num:
  print(i)