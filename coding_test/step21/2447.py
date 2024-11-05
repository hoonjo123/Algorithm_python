#별직기 - 10 (골드5)
#재귀적인 패턴을 재귀함수로 찍는 문제
def drawStars(n):
  if n == 3:
    return ["***","* *","***"]


  prev = drawStars(n//3)
  stars = []


  for i in prev:
    stars.append(i * 3)
  for i in prev:
    stars.append(i + " " * (n//3) + i)
  for i in prev:
    stars.append(i * 3)

  return stars


n = int(input())
result = drawStars(n)
print("\n".join(result))