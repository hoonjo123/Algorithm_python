# 달팽이는 올라가고 싶다
#낮에는 A미터만큼 올라감, 밤에는 B미터 내려감 , (정상에 도달하면 미끄러지지 않는다)
import math
A, B, V = map(int,input().split())

day = math.ceil((V - B)/ (A - B))

print(day)