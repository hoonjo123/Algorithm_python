# 삼각형 외우기

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

total = angle1 + angle2 + angle3

if total != 180:
  print("Error")
elif angle1 == 60 and angle2 == 60 and angle3 == 60:
  print("Equilateral")
elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
    print("Isosceles")
else:
    print("Scalene")