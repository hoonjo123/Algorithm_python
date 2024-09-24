#베르트랑 공준

#n을 입력받고 n보다 크고 2n보다 작거나 같은 소수의 '개수'를 출력

import math
import sys
input = sys.stdin.readline

MaxLimit = 246912
isPrime = [True] * (MaxLimit + 1)
isPrime[0] = isPrime[1] = False

for i in range(2, int(math.sqrt(MaxLimit))+1):
  if isPrime[i]:
    for j in range(i*i,MaxLimit+1, i):
      isPrime[j] = False

while True:
  n = int(input())
  if n == 0:
    break

  count = 0
  for i in range(n+1, 2*n+1):
    if isPrime[i]:
      count+= 1
  
  print(count)