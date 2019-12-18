from collections import deque

# 우, 하, 좌, 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(y,x):
    return 0 <= y < N and 0 <= x < M and data[y][x]

def bfs(sy,sx):
    global ans
    dist = 0
    que = deque()
    visited=[[0]*M for _ in range(N)]
    visited[sy][sx] = 1
    que.append((sy,sx))

    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx) and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                if visited[ny][nx] > dist:
                    dist = visited[ny][nx]
                que.append((ny,nx))
    return dist


N,M = map(int, input().split())
data = [[0]*M for _ in range(N)]
for i in range(N):
    temp = input()
    for j in range(M):
        if temp[j] == "W":
            data[i][j] = 0
        else:
            data[i][j] = 1


ans = 0xfffffff

ans = 0
for i in range(N):
    for j in range(M):
        if data[i][j]:
            path = bfs(i,j)
            if path > ans:
                ans = path

if ans != 0:
    ans -= 1
print(ans)
