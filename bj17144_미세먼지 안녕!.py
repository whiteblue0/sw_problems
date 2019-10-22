from collections import deque

# 우 하 좌 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(y,x):
    return 0<=y<R and 0<=x<C

def diffusion(y,x,initD):
    dust = initD//5
    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if ispass(ny,nx) and data[ny][nx] != -1:
            diffused[ny][nx] += dust
            data[y][x] -= dust

def windup(sy,sx):
    # 상 우 하 좌
    ux = [0, 1, 0, -1]
    uy = [-1, 0, 1, 0]
    d = 0
    data[sy-1][sx] = 0
    y,x = sy-1,sx
    while data[y][x] != -1:
        ny,nx = y+ uy[d],x+ux[d]
        if ispass(ny,nx) and data[ny][nx] == -1:
            break
        elif ispass(ny,nx) and ny <= sy:
            data[y][x] = data[ny][nx]
            data[ny][nx] = 0
        else:
            d += 1
            d %= 4
            ny, nx= y, x
        y,x = ny,nx

def winddown(sy,sx):
    # 하 우 상 좌
    ux = [0, 1, 0, -1]
    uy = [1, 0, -1, 0]
    d = 0
    data[sy+1][sx] = 0
    y,x = sy+1,sx
    while data[y][x] != -1:
        ny,nx = y+ uy[d],x+ux[d]
        if ispass(ny,nx) and data[ny][nx] == -1:
            break
        elif ispass(ny,nx) and ny >= sy:
            data[y][x] = data[ny][nx]
            data[ny][nx] = 0
        else:
            d += 1
            d %= 4
            ny, nx= y, x
        y,x = ny,nx


R,C,T = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(R)]
diffused = [[0]*C for _ in range(R)]
marker = []
cleaner = []

for t in range(T):
    for i in range(R):
        for j in range(C):
            if data[i][j] >= 5:
                marker.append((i, j, data[i][j]))
            elif data[i][j] == -1:
                cleaner.append((i, j))
    for i in range(len(marker)):
        diffusion(marker[i][0], marker[i][1], marker[i][2])
    for i in range(R):
        for j in range(C):
            data[i][j] += diffused[i][j]
            diffused[i][j] = 0
    marker = []
    windup(cleaner[0][0],cleaner[0][1])
    winddown(cleaner[1][0],cleaner[1][1])
result = 0
for i in range(R):
    for j in range(C):
        result += data[i][j]
if result == -2:
    result = 0
else:
    result += 2
print(result)