#소수구하기 
#에라토스테네스의 체 알고리즘!!!
#2부터 시작해서 어떤수가 소수이면, 그 수의 배수를 모두 제거하는것

import math
import sys

input = sys.stdin.readline

def eratostenesAlgorithm(M,N):
  #처음에는 isPrime 리스트에 들어가는 모든 수를 소수라고 가정해서 True라고 설정하기
  isPrime = [True] * (N+1)
  #어차피 0이랑 1은 소수가 아니니 false반환하기
  isPrime[0] = isPrime[1] =False


  #저번에 배웠던 sqrt 함수를 사용해서 n의 제곱근까지의 수를 훑어보기
  for i in range(2, int(math.sqrt(N))+1):
    if isPrime[i]:
      for j in range(i+i,N+1,i):
        isPrime[j]=False

  for i in range(M,N+1):
    if isPrime[i]:
      print(i)

M,N = map(int,input().split())
eratostenesAlgorithm(M,N)