import collections

# 우 하 좌 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(y,x):
    return 0 <= x < M and 0 <= y< N and data[y][x] and not visited[y][x]

def bfs(sy,sx):
    global cnt
    que = collections.deque()
    que.append((sy,sx))
    visited[sy][sx] = 1
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if ispass(ny,nx):
                que.append((ny, nx))
                visited[ny][nx] = 1 + visited[y][x]

N,M = map(int,input().split())
data = [[int(_) for _ in input()]  for _2 in range(N)]
visited = [[0]*M for _ in range(N)]

bfs(0,0)
print(visited[-1][-1])