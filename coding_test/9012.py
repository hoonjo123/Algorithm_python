def isVPS(ps):
  stack = []

  for a in ps:
    if a == '(':
      stack.append(a)
    elif a == ')':
      if stack:
        stack.pop()
      else:
        return "NO"
      
  if len(stack) == 0:
    return "YES"
  else:
    return "NO"


# 파이썬에서 _를 쓰는 이유는 반복만을 중요시할때,
# 사용하지 않는 변수를 사용해서 코드에 혼란을 줄 필요가 없다.

# -- 튜플을 반복할 때 특정 요소를 무시하는 경우 --
# pairs = [(1,2),(3,4),(5,6),(7,8)]
# for _, second in pairs:
#   print(second)

T = int(input())
for _ in range(T):
  ps = input().strip()
  print(isVPS(ps))
