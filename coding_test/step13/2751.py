#수 정렬하기 2
# N = int(input())

# num = []
# for _ in range(N):
#   num.append(int(input()))

# n = int(input())
# res = [int(input().split(" ")) for _ in range(n)]

# b = sorted(set(num))
# # for i in b:
# # print(b)
# # b = sorted(set(num))
# # print(b)
# # num.sort()

# for i in num:
#   print(i)

# sys in out 이용하기
import sys
N = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline()) for _ in range(N)]

numbers.sort()

for i in numbers:
  sys.stdout.write(str(i) + '\n')

#counting sort 이요하기
# import sys
# N = int(sys.stdin.readline())

# count = [0] * 20000001

# for _ in range(N):
#   num = int(sys.stdin.readline().rstrip())
#   count [ num + 1000000 ] += 1

# for i in range(2000001):
  # if count[i] > 0:
    

#list 그냥 출력하는 방법 ( for 문 사용 x )
# lst = [ (10,13) for i in range(1,10,2)]
# lst2 = [ 19 for i in range(1,10)]
# print(*lst,sep='\n')

#문자열 자동으로 인트값으로 변환하여 계산해줌

# temp = "1+3+5"
# print(eval(temp))

#배열에서 인덱스위치 기억할때, 인덱스 위치를 함께 출력해줌
# for idx, i in enumerate(lst):
#   print(idx,i)

# #조합문제에서 많이 쓰임, lst와 lst2를 한번에 출력(lst, lst2)
# for i in zip(lst,lst2):
#   print(i)

# lst.sort(key=lambda x:(x[1],-x[0]))
# lst = sorted([ (10,13) for i in range(1,10)], key= lambda x:x[1])

#dictionary key, value 자동 집어넣기
# from collections import defaultdict
# dic = defaultdict(int)

# for i in range(10):
#   # if i not in dic:
#   #   dic[i] = 1
#   # else:
#   #   dic[i] += 1
#   dic[i] = 1
# print(dic) 