# #덱2
from collections import deque
#
# queue = deque()
#
# N = int(input())
#
# for _ in range(N):
#     command = input().split()
#
#     if command == '1':
#         queue.appendleft()
#     elif command == '2':
#         queue.append()
#     elif command == '3':
#         if queue:
#             queue.popleft()
#         else:
#             print(-1)
#     elif command == '4':
#         if queue:
#             queue.pop()
#         else:
#             print(-1)
#
#     elif command == '5':
#         print(len(queue))
#     elif command == '6':
#         print(1 if not queue else 0)
#     elif command == '7':
#         if queue:
#             print(queue[0])
#     elif command == '8':
#         if queue:
#             print(queue.pop())

#
# queue =deque()
# queue = [1,2,3,4,5]
# queue.pop()

import sys
from collections import deque

# 빠른 입출력을 위한 준비
input = sys.stdin.readline
output = sys.stdout.write

# 덱 생성
dq = deque()

# 명령의 개수 입력
N = int(input())

# 명령 처리
for _ in range(N):
    command = input().split()

    if command[0] == '1':  # 1 X: 덱의 앞에 X를 넣는다
        dq.appendleft(int(command[1]))
    elif command[0] == '2':  # 2 X: 덱의 뒤에 X를 넣는다
        dq.append(int(command[1]))
    elif command[0] == '3':  # 3: 덱의 앞에서 정수를 빼고 출력
        if dq:
            output(f"{dq.popleft()}\n")
        else:
            output("-1\n")
    elif command[0] == '4':  # 4: 덱의 뒤에서 정수를 빼고 출력
        if dq:
            output(f"{dq.pop()}\n")
        else:
            output("-1\n")
    elif command[0] == '5':  # 5: 덱에 있는 정수의 개수 출력
        output(f"{len(dq)}\n")
    elif command[0] == '6':  # 6: 덱이 비어있으면 1, 아니면 0 출력
        output("1\n" if not dq else "0\n")
    elif command[0] == '7':  # 7: 덱의 앞에 있는 정수를 출력
        if dq:
            output(f"{dq[0]}\n")
        else:
            output("-1\n")
    elif command[0] == '8':  # 8: 덱의 뒤에 있는 정수를 출력
        if dq:
            output(f"{dq[-1]}\n")
        else:
            output("-1\n")
