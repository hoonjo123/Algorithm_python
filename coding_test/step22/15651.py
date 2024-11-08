#N과 M 2

def back(numbers):
  if len(numbers) == M:
    print(*numbers)

    return
  
  for i in range(1, N + 1):
      back(numbers + [i])


N, M = map(int,(input().split()))
back([])
