#소트인사이드

# N = int(input())
# numbers = []
# # ltr = [numbers for _ in range(1,N)]
# # print(*ltr, sep= '\n')

# for _ in range(N):
#   numbers.append()

# numbers.sort()
# print(numbers)

N = int(input())

digits = list(str(N))
sorted_digits = sorted(digits, reverse=True)

result = ''.join(sorted_digits)

print(result)