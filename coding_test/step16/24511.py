#queuestack

from collections import deque

def queuestack(N, A, B, M, C):
    
    queue = [deque() for _ in range(N)]
    stack = [[] for _ in range(N)]

    for i in range(N):
        if A[i] == 0:
            queue[i].append(B[i])
        else:
            stack[i].append(B[i])

    results = []

    
    for c in C:
        current = c 
        for i in range(N):
            if A[i] == 0:
                queue[i].append(current) 
                current = queue[i].popleft() 
            else: 
                stack[i].append(current)
                current = stack[i].pop()
        results.append(current)

    return results


N = int(input()) 
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))


result = queuestack(N, A, B, M, C)
print(" ".join(map(str, result)))
