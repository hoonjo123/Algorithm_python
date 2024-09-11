#삼각형과 세 변
while True:
  A, B, C = map(int, input().split())

  if A == 0 and B == 0 and C == 0:
    break


  sides = sorted([A,B,C])

  if sides[0] + sides[1] <= sides[2]:
    print("Invalid")
  elif A == B == C:
    print("Equilateral")
  elif A == B or B == C or A == C:
    print("Isosceles")
  else:
    print("Scalene")