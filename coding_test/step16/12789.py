#도키도키 간식드리미

def canIGetASneak(N, students):
  stack = []
  currentStudent = 1

  for student in students:
    while stack and stack[-1] == currentStudent:
      stack.pop()
      currentStudent += 1

    if student == currentStudent:
      currentStudent += 1
    else:
      stack.append(student)


  while stack and stack[-1] == currentStudent:
    stack.pop()
    currentStudent += 1

  if not stack:
    return "Nice"
  else:
    return "Sad"



N = int(input())
students = list(map(int, input().split()))

print(canIGetASneak(N, students))