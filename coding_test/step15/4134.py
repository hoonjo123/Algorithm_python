#다음 소수
import math
import sys

# #제곱근을 구하는 방법
# num = 25
# root = math.sqrt(num)
# print(root)
# #5.0

def isPrime(num):
  if num < 2:
    return False
  if num == 2:
    return True
  if num % 2 == 0:
    return False
  
  #짝수는 아니기 때문에 3부터 2씩 증가하며 제곱근까지 구하면 된다. range의 특성상 -1까지이기 때문에 +1을 해서 제곱근까지만 소수를 구해본다.
  for i in range(3, int(math.sqrt(num)+1),2):
    #만약 제곱근을 3부터 시작된 i의 수로 나누어 떨어졌다?  그럼 false반환, 왜냐면 예를들어 num이 36이라고 가정한다면
    #3부터 나누어 떨어지니까 false임
    #23같은경우? 3부터 시작... 23 % 3 ? 23 % 4.. 23% 5... 0이 안되므로 True..
    if num % i == 0:
      return False
  return True

def nextPrime(n):
  if n<= 2:
    return 2
  if n % 2 == 0:
    #짝수는 소수가 아니므로 홀수부터 시작함
    n += 1
  while not isPrime(n):
    n += 2
  return n

input = sys.stdin.readline
T = int(input())
for _ in range(T):
  n = int(input())
  print(nextPrime(n))