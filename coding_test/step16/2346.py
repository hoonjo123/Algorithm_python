#풍선 터뜨리기
def balloonGame(N,papers):
  ballons = list(range(1, N+1))
  result = []
  idx = 0

  for _ in range(N):
    result.append(ballons.pop(idx))
    if not ballons:
      break
    move = papers.pop(idx)
    if move > 0:
      idx = (idx + (move -1)) % len(ballons)
    else:
      idx = (idx + move) % len(ballons)

  return result


N = int(input())
papers = list(map(int,input().split()))
print(" ".join(map(str,balloonGame(N,papers))))
  