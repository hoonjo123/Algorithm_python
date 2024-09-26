# 카드 2
from collections import deque

#큐를 사용하여 문제를 풀어보자
#
# 123456
# 23456 =>34562
# 4562 => 5624
# 624 => 246
# 46 => 4

N = int(input())

queue = deque(range(1,N+1))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])