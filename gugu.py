

# def gugu(n):
#   result = []
#   result.append(n*1)
#   result.append(n*2)
#   result.append(n*3)
#   result.append(n*4)
#   return result

# print(gugu(2))

# i = 1
# while i < 10:
#   print(i)
#   i = i + 1


def gugu(n):
  result = []
  i = 1
  while i < 10:
    result.append( n * i )
    i = i + 1
  return result

print(gugu(2))

result = 0
for n in range(1, 1000):
  if n % 3 == 0 or n % 5 == 0:
    result += n
print(result)

#m은 총 게시물의 개수 
#n은 한 페이지당 보여 줄 개수

def get_total_page(m,n):
  if m % n == 0:
    return m // n
  else:
    return m // n + 1
  

print(get_total_page(5, 10))
print(get_total_page(30,10))