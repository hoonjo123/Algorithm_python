# from itertools import permutations

# N, M = map(int, input().split())

# for sequence in permutations(range(1, N + 1), M):
#     print(" ".join(map(str, sequence)))
def backtrack(sequence):
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return

    for i in range(1, N + 1):
        if i not in sequence:  # 중복 방지
            backtrack(sequence + [i])

N, M = map(int, input().split())
backtrack([])
