def num_sum(number):
  return sum(int(digit) for digit in str(number))

def find(target):
  for i in range( 1, target ):
    if i + num_sum(i) == target:
      return i
    
  return 0

N = int(input())
result = find(N)
print(result)