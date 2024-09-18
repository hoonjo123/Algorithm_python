#좌표 정렬하기 2

N = int(input())

coordinate = []

for _ in range(N):
  x, y = map(int, input().split())
  coordinate.append((x, y))


sortedCoordinate = sorted(coordinate, key= lambda coord:(coord[1],coord[0]))

for x, y in sortedCoordinate:
  print(x, y)