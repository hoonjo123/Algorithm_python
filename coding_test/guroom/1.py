#1번 [대학] 왜 아픈 상처에 소금을 뿌리십니까?

# 낙화라는 시를 좋아했던 구름이. 돌뿌리에 걸려 넘어짐
# 가능한 한 크기가 작으면서 모든 상처를 덮을 수 있는 반창고 한개를 구매할 것
# n*n크기의 정사각형 모양, 한칸은 1*1의 반창고가 필요 ㅎ


# 상처가 있는 칸들을 찾기, 상처가 있는 테두리를 찾아 둘레 합하면 될것같음

# 가로 = 오른쪽 -왼쪽 +1
# 세로 = 아래 - 위 + 1


# def findSize(n, grid):
#   top, bottom = n, -1
#   left, right = n, -1

#   for i in range(n):
#     for j in range(n):
#       if grid[i][j] == '1':
#         top = min(top, i)
#         bottom = max(bottom, i)
#         if left == n:
#           left = j
#         left = min(left, j)
#         right = max(right, j)

#   height = bottom - top + 1
#   width = right - left + 1

#   return 2 * (height + width)

# n = int(input())
# grid = [input().split() for _ in range(n)]

# print(findSize(n, grid))

def find_minimum_patch_size(n, grid):
    top, bottom = n, -1
    left, right = n, -1
    
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '1':
                top = min(top, i)
                bottom = max(bottom, i)
                left = min(left, j)
                right = max(right, j)
    
    if top == n: 
        return 0
    
    width = right - left + 1
    height = bottom - top + 1
    
    
    return width * height


n = int(input())  
grid = [input().split() for _ in range(n)] 


print(find_minimum_patch_size(n, grid))

