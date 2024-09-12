#영화감독 숌


#숫자로는 구별하기 힘드니 문자열로 바꿔주다.
def isEndNumber(num):
  return '666' in str(num)


def nEndNumber(N):
  endCount = 0
  num = 666
  while True:
    if isEndNumber(num):
      endCount += 1
      if endCount == N:
        return num
    
    num += 1

N = int(input())

result = nEndNumber(N)
print(result)