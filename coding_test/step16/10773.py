#제로
#0을 입력하면 스택의 pop일 이용하면 될것같다. 그러고 나서 출력해주면 될것같다. 합으로
import sys

input = sys.stdin.readline

K = int(input())

stack = []
results = 0
for _ in range(K):
  numbers = int(input())
  if numbers == 0:
    stack.pop()
  else:
    stack.append(numbers)
    # for i in range(len(stack)):
    #   results += i

results = sum(stack)

print(results)