#칸토어 집합
import sys

def kantor(n):
  if n == 0:
    return '-'
  
  pre = kantor(n-1)
  remove = ' ' * len(pre)
  return pre + remove + pre

for line in sys.stdin:
  n = int(line)
  print(kantor(n))