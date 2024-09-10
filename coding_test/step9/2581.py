#소수

def isPrime(number):
  if number == 1:
    return False
  
  for i in range(2, number):
    if number % i == 0:
      return False
    
  return True

M = int(input())
N = int(input())

primes = []
for number in range(M, N + 1):
  if isPrime(number):
    primes.append(number)

if primes:
  print(sum(primes))
  print(min(primes))
else:
  print(-1)