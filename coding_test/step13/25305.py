#커트라인
N, k = map(int, input().split())
grades = list(map(int,input().split()))

grades.sort(reverse=True)

print(grades[k - 1])