#좌표 압축??

# 주어진 숫자들의 상대적인 크기 순서만 유지하면서 그 숫자들을 0부터 시작하는 연속된 정수로 변환하는 것
# 2 4 -10 4 -9 가 있다고 가정한다면
# 오름차순으로 먼저 정렬해보자 -10 -9 2 4 4
# 정렬된 순서대로 0부터 시작하는 새로운 번호를 매긴다.


# -10 : 0 (가장 작은 숫자 0부터 시작)
# -9 : 1
# 2 : 2
# 4: 3
# 4: 3

# 2    4 -10 4 -9
# -10 -9 2   4  4

# 2는 세번째 위치에 있었으므로 2
# 4는 네번째 위치에 있었으므로 3
# -10 같은 개념으로 0
# 4는 네번째 위치해 있으므로 3
# -9는 두번째 위치해 있으므로 1

# 최종 결과 2 3 0 3 1

import sys

N = int(sys.stdin.readline())
coordinates = list(map(int, sys.stdin.readline().split()))

#여기에서 list(map)과 map()의 차이를 이해해보자
# list(map())을 사용했는데, 그 이유는:

# 입력된 좌표들에 여러 번 접근해야 함
# 인덱싱이 필요함

# map(int, sys.stdin.readline().split())

# 이것은 map 객체를 반환함
# map 객체는 이터레이터(iterator)로, 필요할 때만 값을 생성(lazy evaluation).
# 메모리 효율적이지만, 한 번만 순회할 수 있음


# list(map(int, sys.stdin.readline().split()))

# 이것은 map의 결과를 리스트로 변환
# 모든 값이 즉시 메모리에 로드 됨
# 메모리를 더 사용하지만, 여러 번 접근하거나 인덱싱이 가능함

indexed_coords = list(enumerate(coordinates))
# 예를 들어: [(0, 2), (1, 4), (2, -10), (3, 4), (4, -9)]

# coordinates = [100, 200, 300]
# indexed_coords = list(enumerate(coordinates))
# print(indexed_coords)
# # 출력: [(0, 100), (1, 200), (2, 300)]

# 이런것도 가능! 
# list(enumerate(coordinates, start=1))
# 출력: [(1, 100), (2, 200), (3, 300)]

# enumerate()는 특히 리스트의 인덱스와 값을 동시에 다룰 때 매우 유용

sortedCoordinates = sorted(indexed_coords, key=lambda x: x[1])

compressedCoordinates = [0] * N #n개의 0으로 채워진 리스트 만들기
rank = 0 #현재 순위 0 초기화
prev = None #이전 좌표값저장

for i, coordinate in sortedCoordinates:
  if coordinate != prev:
    rank += 1
  compressedCoordinates[i] = rank -1
  prev = coordinate

print(*compressedCoordinates)

#입력이 [2, 4, -10, 4, -9]일 때:

# 정렬 후: [-10, -9, 2, 4, 4]
# 압축 과정:

# -10 → 0 (rank 1 - 1 = 0)
# -9  → 1 (rank 2 - 1 = 1)
# 2   → 2 (rank 3 - 1 = 2)
# 4   → 3 (rank 4 - 1 = 3)
# 4   → 3 (같은 값이므로 rank 증가 없음)


# 결과: [2, 3, 0, 3, 1] (원래 순서로)

#*의 용도 : 리스트 , 튜플을 언패킹해주는 용도임 []이렇게 되어있는게 그냥 ''.join(map(str, compressed))
#로 나오는거임