#세 막대

a, b, c = map(int, input().split())

sides = sorted([a, b, c], reverse=True)

if sides[0] >= sides[1] + sides[2]:
  sides[0] = sides[1] + sides[2] -1

perimeter = sum(sides)

print(perimeter)