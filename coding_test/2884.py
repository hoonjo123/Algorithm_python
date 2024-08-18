
# H, M = map(int,input().split())

# M -= 45

# if H < 0:
#   H = 23

# if H == 0:
#   H = 24

# if M < 0:
#   M += 60
#   H -= 1

# # if M == 0:
# #   M == 0

# print(H,M)

H, M = map(int, input().split())

M -= 45  # 먼저 분에서 45분을 뺍니다.

if M < 0:  # 만약 분이 음수가 되면
    M += 60  # 60분을 더해주고
    H -= 1  # 시(hour)에서 1시간을 뺍니다.

if H < 0:  # 시가 음수가 되는 경우 (예: 0시에서 1시간을 빼는 경우)
    H = 23  # 시를 23으로 설정합니다.

print(H, M)
