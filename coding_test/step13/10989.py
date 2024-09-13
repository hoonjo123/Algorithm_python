#수 정렬하기 3

# import sys
# N = int(sys.stdin.readline())

# numbers = []
# for _ in range(N):
#   numbers.append(int(sys.stdin.readline()))

# numbers.sort()

# for num in numbers:
#   sys.stdout.write(str(num)+'\n')

import sys
N = int(sys.stdin.readline())

count = [0] * 10001

for _ in range(N):
  num = int(sys.stdin.readline())
  count[num] += 1

for i in range(10001):
  if count[i] > 0:
    for _ in range(count[i]):
      sys.stdout.write(str(i)+'\n')