# 대표값2
numbers = []
for _ in range(5):
  numbers.append(int(input()))


avg = sum(numbers) // len(numbers)

numbers.sort()

middle = numbers[len(numbers)// 2]

print(avg)
print(middle)