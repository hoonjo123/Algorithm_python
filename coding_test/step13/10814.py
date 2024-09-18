#나이순 정렬

# 회원들의 나이가 증가하는순으로
# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서


N = int(input())

members = []

for i in range(N):
  age, name = input().split()
  members.append((int(age), i, name))

sortedMembers = sorted(members, key=lambda x: (x[0],x[1]))

for age,_,name in sortedMembers:
  print(age, name)