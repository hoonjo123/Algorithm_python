#영단어 암기는 괴로워

import sys
from collections import Counter

input = sys.stdin.readline
N, M = map(int, input().split())

words = []
for _ in range(N):
  word = input().strip()
  if len(word) >= M:
    words.append(word)

counter = Counter(words)
# print(words)

sortedWords = sorted(counter.keys(), key = lambda x: (-counter[x], -len(x), x))

for word in sortedWords:
  print(word)