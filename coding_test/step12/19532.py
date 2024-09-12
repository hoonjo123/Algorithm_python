a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
  for y in range(-999, 1000):
    if a*x + b*y == c and d*x + e*y == f:
      print(x, y)
      exit()

# ax + by = c
# dx + ey = f

#크래머의 법칙으로 연립방정식을 행렬식을 이용해 해결하는 방법
#x = ce - bf /ae - bd
#y = af -cd / ae - bd
# 연립방정식의 기본 형태:
#ax + by = c dx + ey = f

