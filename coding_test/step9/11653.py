#소인수분해

#1보다 큰 자연수를 소수인 인수 들만의 곱으로 나타내는 것 

N = int(input())

divisor = 2

while N > 1:
  if N % divisor == 0:
    print(divisor)
    N = N //divisor
  else:
    divisor += 1