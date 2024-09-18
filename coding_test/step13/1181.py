#단어정렬

# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 정렬하는 프로그램
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

N = int(input())

words = set()

for _ in range(N):
  word = input().strip()
  words.add(word)


sortedWords = sorted(words, key=lambda x: (len(x),x))

for word in sortedWords:
  print(word)