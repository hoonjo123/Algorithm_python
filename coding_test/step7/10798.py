#세로읽기

vocas = []
for _ in range(5):
  vocas.append(input().strip())

result = []

for i in range(15):
  for voca in vocas:
    if i < len(voca):
      result.append(voca[i])


print("".join(result))