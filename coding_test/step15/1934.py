import math

T = int(input())

for _ in range(T):
  A, B = map(int,(input().split()))
  
  gcd = math.gcd(A,B)
  lcm = (A*B) // gcd

  print(lcm)


#최소공배수는 최대공약수로 구할 수 있다
  #LCM(A,B) = A*B / GCD(A,B)



