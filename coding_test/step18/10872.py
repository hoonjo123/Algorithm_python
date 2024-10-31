#팩토리얼
def factorial(N):
  result = 1
  for i in range(2, N+1):
    result *= i
  return result


N = int(input())
print(factorial(N))