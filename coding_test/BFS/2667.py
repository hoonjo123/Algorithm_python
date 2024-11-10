#단지번호 붙이기
from collections import deque

def bfs(si, sj):
  q = deque()
  q.append((si, sj))
  # v[si][sj] = 1
  arr[si][sj] = 0
  cnt = 1

  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  while q:
    ci,cj = q.popleft()
    for di,dj in directions:
      ni,nj = ci+di, cj+dj
      if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
        q.append((ni,nj))
        arr[ni][nj] = 0
        cnt += 1
  
  return cnt


N = int(input())
arr = [list(map(int,input().strip())) for _ in range(N)]
# v = [[0]*N for _ in range(N)]
ans = []

for i in range(N):
  for j in range(N):
    if arr[i][j] == 1:
      ans.append(bfs(i,j))


ans.sort()
print(len(ans))
print(*ans, sep='\n')
