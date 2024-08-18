MOD = 10**9 + 7

# 세그먼트 트리 초기화
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = (self.tree[2 * node + 1] + self.tree[2 * node + 2]) % MOD
    
    def update_range_add(self, node, start, end, l, r, val):
        if start > r or end < l:
            return
        if start == end:
            self.tree[node] = (self.tree[node] + val) % MOD
            return
        mid = (start + end) // 2
        self.update_range_add(2 * node + 1, start, mid, l, r, val)
        self.update_range_add(2 * node + 2, mid + 1, end, l, r, val)
        self.tree[node] = (self.tree[2 * node + 1] + self.tree[2 * node + 2]) % MOD
    
    def query_sum(self, node, start, end, l, r):
        if start > r or end < l:
            return 0
        if start >= l and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query_sum(2 * node + 1, start, mid, l, r)
        right_sum = self.query_sum(2 * node + 2, mid + 1, end, l, r)
        return (left_sum + right_sum) % MOD

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))
m = int(input())

segment_tree = SegmentTree(arr)

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y, v = query[1] - 1, query[2] - 1, query[3]
        segment_tree.update_range_add(0, 0, n - 1, x, y, v)
    elif query[0] == 4:
        x, y = query[1] - 1, query[2] - 1
        result = segment_tree.query_sum(0, 0, n - 1, x, y)
        print(result)
