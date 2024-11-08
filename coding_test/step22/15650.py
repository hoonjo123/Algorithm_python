#N과 M 2

def back(numbers,start):
  if len(numbers) == M:
    sorted(numbers)
    print(*numbers)

    return
  
  for i in range(start, N + 1):
    if i not in numbers:
      back(numbers + [i], i + 1)


N, M = map(int,(input().split()))
back([],1)