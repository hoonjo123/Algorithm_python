# 진법변환2

# result = ['A','B','C']
# print(''.join(result[::-1]))
#CBA -> 리스트를 뒤집는 방법 result :: -1

def decimal(N,B):
  digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  result = []

  while N > 0:
    result.append(digits[N%B])
    N //= B
    # //는 몫 연산자, 즉, N= N// B 
  
  return ''.join(result[::-1])

N, B = map(int, input().split())
print(decimal(N, B))
