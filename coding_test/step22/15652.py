#N과 M 4

def backtracking(numbers):
  if len(numbers) == M:
    print(*numbers)
    return



  # if numbers:
  #   start = numbers[-1]
  # else:
  #   start = 1

  #n = 4
  #m = 2
  start = numbers[-1] if numbers else 1
  for i in range(start, N+1):
      backtracking(numbers + [i])

N, M = map(int,input().split())
backtracking([])

# i = 1~4
# i = 1 : back([1] + [1])
# i = 2 : back([1, 1]) => 출력
