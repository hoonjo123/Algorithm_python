#약수 구하기

def yaksoo(N, K):
  yaksoo = []
  for i in range(1, N + 1):
    if N % i == 0:
      yaksoo.append(i)
    if len(yaksoo) == K:
      return yaksoo[-1]
  
  # 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.
  return 0 if len(yaksoo) < K else yaksoo[K - 1]

N, K = map(int, input().split())

result = yaksoo(N, K)

print(result)