#촌수계산

#BFS 문제
#visited배열을 얼마나 걸쳐갔는지 계산해주면 될것같다
#도달불가할때는 -1

def bfs(s, e):
  global n
  q = []
  v = [0] * (n+1)

  q.append(s)
  v[s] = 1

  while q:
    c = q.pop(0)
    if c == e:
      return v[e]-1

    for n in adj[c]:
      if not v[n]:
        q.append(n)
        v[n] += v[c] + 1
    
  return -1

n = int(input())
s, e = map(int,input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
  x, y = map(int,input().split())
  adj[x].append(y)
  adj[y].append(x)

ans = bfs(s, e)
print(ans)