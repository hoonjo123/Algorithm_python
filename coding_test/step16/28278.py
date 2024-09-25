#스택, 큐, 덱

#스택2

import sys
input = sys.stdin.readline

stack = []

N = int(input())
for _ in range(N):
  command = input().split()

  if command[0] == '1':
    stack.append(int(command[1]))
  elif command[0] == '2':
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif command[0] == '3':
    print(len(stack))
  elif command[0] == '4':
    print(1 if not stack else 0)
  elif command[0] == '5':
    if stack:
      print(stack[-1])
    else:
      print(-1)