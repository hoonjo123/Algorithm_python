#회사에 있는 사람
import sys

input = sys.stdin.readline

n = int(input())

isWorking = set()

for _ in range(n):
  name, act = input().split()
  if act == "enter":
    isWorking.add(name)
  elif act == "leave":
    isWorking.remove(name)

workerSorted = sorted(isWorking, reverse=True)

for name in workerSorted:
  print(name)