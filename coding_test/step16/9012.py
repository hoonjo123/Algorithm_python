#괄호

# ( 랑 )이게 한쌍으로 이루어져 있으면 YES 아니면 NO
#한쌍인지 어떻게 알 수 있을까?

T = int(input())

for _ in range(T):
  Parentheses = input().strip()
  stack = []
  isCouple = True

  for char in Parentheses:
    if char == '(':
      stack.append(char)
    elif char == ')':
      if stack:
        stack.pop()
      else:
        isCouple = False
        break

  if stack:
    isCouple = False

  if isCouple:
    print("YES")
  else:
    print("NO")