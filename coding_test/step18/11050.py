#이항계수 1 

#n개의 서로다른 것들 중에서 k개를 선택하는 것의 조합의 경우의 수를 구하는 것.

#즉, nCk 로 나타낼 수 있다
#nCk = factorial(n) // (facotrial(k) * factorial(n-k))


import sys
input = sys.stdin.readline

def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)

n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n-k)))