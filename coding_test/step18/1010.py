#다리 놓기
import sys
import math

input = sys.stdin.readline


def bridge(N,M):
  return math.comb(M,N)

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  print(bridge(N,M))