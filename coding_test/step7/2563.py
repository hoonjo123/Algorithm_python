#색종이

#0으로 채워진 도화지 만들기 000000000000000...100x100
paper = [[0]*100 for _ in range(100)]

#색종이수

n = int(input())

for _ in range(n):
  x, y = map(int, input().split())
  for i in range(x, x + 10):
    for j in range(y, y + 10):
      paper[i][j] = 1


area = 0
for row in paper:
  area += sum(row)

print(area)