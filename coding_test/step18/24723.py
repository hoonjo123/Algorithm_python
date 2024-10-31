#녹색거탑

#각 층마다 경우의 수가 두배 씩 증가 
def countDp(N):
  dp = [0] * (N + 1)

  dp[1] = 2

  for i in range(2, N + 1):
    dp[i] = dp[i - 1] * 2

  return dp[N]


N = int(input())
print(countDp(N))