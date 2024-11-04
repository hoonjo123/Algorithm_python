#팩토리얼 2
#팩토리얼은 단순 for문으로도 구할 수 있지만, 학습을 위해 재귀를 써 봅시다

def factorial(N):
  if N < 2:
    return 1
  else:
    return N * factorial(N - 1)
  

N = int(input())
  
print(factorial(N))