#숫자 카드 2
from collections import Counter

N = int(input())
cards = list(map(int,input().split()))

M = int(input())
whatIsInCards = list(map(int, input().split()))

haveCounts = Counter(cards)
result = [haveCounts[i] for i in whatIsInCards]

print(*result)

#딕셔너리 해시맵을 사용한 풀이법
#숫자의 등장 횟수를 빠르게 기록하고 검색가능

