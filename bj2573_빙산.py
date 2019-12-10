from collections import deque
# 우, 하, 좌, 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(y,x):
    return 0<=y<N and 0<=x<M and data[y][x] and not visited[y][x]

def bfs(sy,sx):
    global cnt, flag
    que = deque()
    visited[sy][sx] = cnt
    if cnt > 1:
        flag = True
        return
    que.append((sy,sx))
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx):
                visited[ny][nx] = cnt

                que.append((ny,nx))
    cnt += 1



N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
iceberg = []


icemax = 0
for i in range(N):
    for j in range(M):
        if data[i][j]:
            iceberg.append([i,j,data[i][j]])
        if data[i][j] > icemax:
            icemax = data[i][j]

result = 0

for t in range(icemax+1):
    visited = [[0] * M for _ in range(N)]
    cnt = 1
    flag = False
    for i in range(len(iceberg)):
        if ispass(iceberg[i][0],iceberg[i][1]):
            bfs(iceberg[i][0],iceberg[i][1])
            if flag:
                break
    if flag:
        result = t
        break

    if not flag:
        for i in range(len(iceberg)):
            ice = iceberg[i][2]
            water = 0
            y = iceberg[i][0]
            x = iceberg[i][1]
            for j in range(4):
                ny,nx = y+dy[j],x+dx[j]
                if data[ny][nx] == 0:
                    water += 1
            if ice > water:
                ice -= water
            else:
                ice = 0
            iceberg[i][2] = ice
        for i in range(len(iceberg)):
            y = iceberg[i][0]
            x = iceberg[i][1]
            data[y][x] = iceberg[i][2]

print(result)
