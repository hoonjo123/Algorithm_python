# 소수 찾기


#소수란? 1과 자기자신만을 약수로 갖는 수를 소수라고 한다
#참고로 1은 소수가 아님


def isPrime(number):
  if number == 1:
    return False
  
  for i in range(2, number):
    if number % i == 0:
      return False
    
  return True


N = int,input()
numbers = list(map(int, input().split()))

count = 0
for number in numbers:
  if isPrime(number):
    count += 1

print(count)