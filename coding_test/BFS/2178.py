#미로탐색
import sys

#si, sj = start i, start j
#ei, ej = end i , end j
#ni, nj = next i, next j
#ci, cj + current i, current j


def bfs(si, sj, ei, ej):
  q = []
  v = [[0]*M for _ in range(N)]

  q.append((si,sj))
  v[si][sj] = 1

  while q:
    ci, cj = q.pop(0)
    if(ci,cj) ==(ei,ej):
      return v[ei][ej]


#전형적인 bfs 패턴, 4방향 탐색하는 좌표
    
    for di,dj in ((-1,0), (1,0), (0,-1),(0,1)):
      ni, nj = ci+di, cj+dj
      #조건에 맞으면: arr == 1(길어거나) , v == 0(방문하지 않았거나)
      if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and v[ni][nj] == 0:
        q.append((ni,nj))
        v[ni][nj] = v[ci][cj]+1 


N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]

ans = bfs(0, 0, N-1, M-1)
print(ans)

