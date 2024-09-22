def repaint(board, x, y):
  count1 = 0
  count2 = 0
  for i in range(8):
    for j in range(8):
      if ( i + j ) % 2 == 0:
        if board[x+i][y+j] != 'W':
          count1 += 1
        if board[x+i][y+j] != 'B':
          count2 += 1

      else:
        if board[x+i][y+j] != 'B':
          count1 += 1
        if board[x+i][y+j] != 'W':
          count2 += 1
  
  return min(count1,count2)


N, M = map(int,input().split())
board = [input() for _ in range(N)]

minRepaint = 64
for i in range(N-7):
  for j in range(M-7):
    minRepaint = min(minRepaint, repaint(board, i, j))

print(minRepaint)