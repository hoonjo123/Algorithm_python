#나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

N, M = map(int, input().split())


NumToName = {}
NameToNum = {}

for i in range(1, N + 1):
  name = input().strip()
  NumToName[i] = name
  NameToNum[name] = i

for _ in range(M):
  query = input().strip()
  if query.isdigit():
    print(NumToName(int[query]))
  else:
    print(NameToNum[query])

# is digit()
#해당 문자열이 숫자로만 이루어져 있는지 확인.
    #만약 숫자로만 이루어져 있다면?
    #숫자를 이름으로 변환

    #그렇지 않고 문자가 포함되어 있다면? 이름을 숫자로 변환

