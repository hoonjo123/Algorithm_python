#창문 닫기

# 1번째 사람은 1의 배수 번째 창문이 열려있으면 닫고 닫혀있으면 연다. 1, 1, 1
# 창문을 여는건 1, 닫는건 0
# 2번째 사람은 2의 배수를 닫는다고 함 => 1, 0 , 1
# 3번째 사람은 3의 배수를 닫음 => 1,0, 0

# 모든 창문은 닫혀 있다고 함 즉, 0 0 0 0 ... 으로 
# 4번째 사람은 4의 배수를 닫음 

# 사람수와 창문의 수는 동일함
# 만약 5라고 한다면

# 0 0 0 0 0

# 1 => 1 1 1 1 1
# 2 => 1 0 1 0 1
# 3 => 1 0 0 0 1
# 4 => 1 0 0 1 1

# N = int(input())
# openWindow = []
# for _ in range(N):
#   openWindow.append(0)

# def changeNumber(num):
#   if openWindow[i] == 0:
#     openWindow[i] == 1

# print(openWindow)
#1의 배수일 경우 무조건 0을 1로
#2의 배수일 경우 리스트의 2의 짝수부분을 0일경우 1로, 1일경우 0으로
#3의 배수일 경우 리스트의 3의 배수 부분 0 일경우 1로, 1일경우 0으로

#해당 문제는 완전제곱수를 기반으로 풀어보자
#완전 제곱수 = k의 제곱과 같은 형태
# 이때 k는 N의 제곱근을 의미

import math
import sys
input = sys.stdin.readline

N = int(input())

result = int(math.sqrt(N))
print(result)