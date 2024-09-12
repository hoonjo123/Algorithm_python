#설탕 배달

def sugarPlasticBags(N):
  for fiveKg in range(N//5, -1, -1):
    remain = N - ( 5 * fiveKg )
    #if N == 3이라면 5, 10
    if remain % 3 == 0:
      threeKg = remain // 3
      return fiveKg + threeKg
  return -1

N = int(input())
result = sugarPlasticBags(N)
print(result)
