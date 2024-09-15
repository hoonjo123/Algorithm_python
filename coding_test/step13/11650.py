#좌표 정렬하기

N = int(input())

coordinate = []

for _ in range(N):
  x, y = map(int, input().split())
  coordinate.append((x, y))

sortedCoordinate = sorted(coordinate,key=lambda coord: (coord[0], coord[1]))

for x, y in sortedCoordinate:
  print(x, y)


#정렬 sort와 sorted
  

# sortedList = [1,2,5,3,5,3,4,25,34]
# result = sorted(sortedList, reverse=True)
# print("result: ", result)
# print("원본",sortedList)