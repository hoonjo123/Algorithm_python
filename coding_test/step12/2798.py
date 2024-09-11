#블랙잭

N, M = map(int, input().split())
cards = list(map(int, input().split()))


result = 0

for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      sum_card = cards[i] + cards[j] + cards[k]
      # result += sum_card
      if sum_card <= M and sum_card > result:
        result = sum_card

print(result)