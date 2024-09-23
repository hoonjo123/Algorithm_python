#소수구하기 
#에라토스테네스의 체 알고리즘!!!
#2부터 시작해서 어떤수가 소수이면, 그 수의 배수를 모두 제거하는것

import math
import sys

input = sys.stdin.readline

def eratostenesAlgorithm(M,N):
  isPrime = [True] * (N+1)
  isPrime[0] = isPrime[1] =False

  for i in range(2, int(math.sqrt(N))+1):
    if isPrime[i]:
      for j in range(i+i,N+1,i):
        isPrime[j]=False

  for i in range(M,N+1):
    if isPrime[i]:
      print(i)

M,N = map(int,input().split())
eratostenesAlgorithm(M,N)