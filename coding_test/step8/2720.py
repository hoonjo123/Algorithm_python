# 세탁소 사장 동혁

# Quarter = 0.25
# Dime = 0.10
# Nickel = 0.05
# Penny = 0.01

T = int(input())

for _ in range(T):
  C = int(input())
  
  Quarter = C//25
  C %= 25

  Dime = C // 10
  C %= 10

  Nickel = C // 5
  C %= 5

  Penny = C

  print(Quarter, Dime, Nickel, Penny)