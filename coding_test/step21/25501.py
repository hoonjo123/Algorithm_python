#재귀의 귀재
#재귀의 동작을 파악하는 문제. 이 문제의 설명을 팰린드롬으로 쓰실 수 있는 분이 계신다면 요청 게시판에 건의 바랍니다. 감사합니다.

def recursion(s, l, r):
  global cnt
  cnt += 1

  if l >= r: return 1
  elif s[l] != s[r]: return 0
  else: return recursion(s, l+1, r-1)

def isPalindrome(s):
  return recursion(s, 0, len(s)-1)


T = int(input())
for _ in range(T):
  cnt = 0
  print(isPalindrome(input().rstrip()),cnt)