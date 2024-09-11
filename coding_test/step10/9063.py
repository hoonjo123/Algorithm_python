#대지

N = int(input())

xpoint = []
ypoint = []

for i in range(N):
  x, y = map(int, input().split())
  xpoint.append(x)
  ypoint.append(y)

width = max(xpoint) - min(xpoint)
height = max(ypoint) - min(ypoint)

square = width * height

print(square)