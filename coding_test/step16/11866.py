#요세푸스 문제 0

#큐를 이용해서 배열을 푸는 문제
from collections import deque


N, K = map(int,input().split())

people = deque(range(1, N + 1))

result = []

while people:
    people.rotate(-(K-1))
    result.append(people.popleft())

print("<" + ", ".join(map(str, result)) +">")




