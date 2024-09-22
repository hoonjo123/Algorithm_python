#분수 합

#기약분수란? 더 이상 약분할 수 없는 분수

#최대공약수 구해서 나눠주기

import math

a1, b1 = map(int,input().split())

a2, b2 = map(int,input().split())

commonBottom = b1 * b2
commonSum = a1 * b2 + a2 * b1

gcd = math.gcd(commonSum, commonBottom)

resultTop = commonSum // gcd
resultBottom = commonBottom // gcd

print(resultTop, resultBottom)