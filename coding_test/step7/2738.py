# 행렬덧셈

#N과 M 입력받기 엔은 행 엠은 열
N, M = map(int, input().split())

#N개의 줄에 원소 M개

A = []
for _ in range(N):
  row = list(map(int, input().split()))
  A.append(row)

  
B = []
for _ in range(N):
  row = list(map(int, input().split()))
  B.append(row)


result = []
for i in range(N):
  row = []
  for j in range(M):
    row.append(A[i][j] +  B[i][j])
  result.append(row)


for row in result:
  print(" ".join(map(str, row)))