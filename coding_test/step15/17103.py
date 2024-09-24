#골드바흐 파티션
#두 소수 p와 q의 합으로 짝수 N을 나타내는 것
import sys
import math

MaxLimit = 1000000
isPrime = [True] * (MaxLimit + 1)
isPrime[0] = isPrime[1] = False


for i in range(2, int(math.sqrt(MaxLimit)) + 1):
  if isPrime[i]:
    for j in range(i*i,MaxLimit+1,i):
      isPrime[j] = False

T = int(input())

for _ in range(T):
  N = int(input())
  count = 0 

#n//2까지 검사하는 이유
  # 중복을 방지하기 위해 해당 범위까지만 검사함
  # N = 10이라고 가정하면 p+q = N을 만족하는 소수 쌍을 알아보자
  # p = 3 , q = N - 3 = 7
  # p = 5 , q = N - 5 = 5
  # p = 7, q = N - 7 = 3 (이미 계산을 했다. 중복되는것을 확인 가능)
  # 즉, p<=q라는 조건이 성립한다. 
  for i in range(2, N//2 + 1):
    if isPrime[i] and isPrime[N - i]:
      count+=1


  print(count)
