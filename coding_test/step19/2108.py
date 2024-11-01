#통계학
import sys
from collections import Counter

input = sys.stdin.readline
N = int(input().strip())
numbers = [int(input().strip()) for _ in range(N)]

average = round(sum(numbers) / N)

numbers.sort()
middleValue = numbers[N//2]

counter = Counter(numbers)
# most_common은 빈도가 높은 값들을 내림차순으로 정렬한 리스트를 반환한다.
mostCommon = counter.most_common()
maxFrequency = mostCommon[0][1]

# numbers = [1,1,2,2,3]
# Counter(numbers) => {1: 2, 2: 2, 3: 1}

frequencyValues = []
for num, freq in mostCommon:
  if freq == maxFrequency:
    frequencyValues.append(num)

if len(frequencyValues) > 1:
  mode = sorted(frequencyValues)[1]
else:
  mode = frequencyValues[0]


rangeValue = max(numbers) - min(numbers)

print(average)
print(middleValue)
print(mode)
print(rangeValue)