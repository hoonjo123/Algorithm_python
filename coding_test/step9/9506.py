#약수들의 합

# while True:
#   n = int,input()
#   yaksoo = []

#   for i in range(1, n):
#     if n % i == 0:
#       yaksoo.append(i)
    
#   yaksoo.sort
#   for j in range(yaksoo):
#     if j.yaksoo == 


def isPerfect(n):
  yaksoo = []
  
  for i in range(1, n):
      if n % i == 0:
        yaksoo.append(i)
  return yaksoo


while True:
  n = int(input())
  if n == -1:
    break

  yaksoo = isPerfect(n)

  if sum(yaksoo)==n:
    print(f"{n} = {' + '.join(map(str, yaksoo))}")
  else:
    print(f"{n} is NOT perfect.")
  