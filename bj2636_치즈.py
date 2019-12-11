from collections import deque

# 우, 하, 좌, 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ismelt():
    for i in range(N):
        for j in range(M):
            if data[i][j]:
                return False
    return True

def ischeese(y,x):
    return 0 <= y < N and 0 <= x < M and data[y][x] and not touched[y][x]

def isair(y,x):
    return 0<=y<N and 0<=x<M and not data[y][x] and not visited[y][x]

def bfs(sy,sx):
    global melt
    que = deque()
    visited[sy][sx] = 1
    que.append((sy,sx))
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if isair(ny,nx):
                visited[ny][nx] = 1
                que.append((ny,nx))
            if ischeese(ny,nx):
                touched[ny][nx] = 1
                melt.append([ny,nx])


N,M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]



t = 0


while True:
    if ismelt():
        break
    melt = []
    visited = [[0] * M for _ in range(N)]
    touched = [[0] * M for _ in range(N)]
    bfs(0, 0)
    cheesecnt = len(melt)
    for i in range(len(melt)):
        y = melt[i][0]
        x = melt[i][1]
        data[y][x] = 0
    t += 1
print(t)
print(cheesecnt)