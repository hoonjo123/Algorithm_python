#최댓값

#<그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 
#이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

grid = []
for _ in range(9):
  grid.append(list(map(int,input().split())))

#문제에서보면 자연수 또는 0,,, 초기값을 0으로 지정했다 가정했을 때 만약 자연수가 전부 0이라면 오류가 발생함
  # 가장 작은 수인 -1로 초기화를 해주는게 맞음 
max_value = -1
max_row = -1
max_col = -1

for i in range(9):
  for j in range(9):
    if grid[i][j] > max_value:
      max_value = grid[i][j]
      max_row = i + 1 
      max_col = j + 1


print(max_value)
print(max_row,max_col)