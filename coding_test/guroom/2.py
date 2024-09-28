#불공정 선거

n = int(input())
getFavorites = [0]*9

moreImportant = {'A':3,'B':2,'C':1}

for _ in range(n):
  alphabet, candidate = input().split()
  candidate = int(candidate) -1
  getFavorites[candidate] += moreImportant[alphabet]


maxFavorites = max(getFavorites)
winnerIs = getFavorites.index(maxFavorites) + 1

print(winnerIs)