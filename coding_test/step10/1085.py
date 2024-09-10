# 직사각형에서 탈출

x, y, w, h = map(int, input().split())

dtoleft = x
dtoright = w - x
dtotop = h - y
dtobottom = y

minD = min(dtoright, dtobottom,dtoleft,dtotop)
print(minD)