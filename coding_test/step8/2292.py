N = int(input())

if N == 1:
  print(1)
else:
  count = 1
  roomNumber = 1

  while N > roomNumber:
    roomNumber += 6 * count
    count += 1
  print(count)