from collections import deque

# 우 하 좌 상
dx = [1,0,-1,0,]
dy = [0,1,0,-1,]

def ispass(ny,nx,y,x):
    return 0<=ny<N and 0<=nx<M and visited[ny][nx] > visited[y][x] + data[y][x]

def bfs():
    sy,sx = 0,0
    que = deque()
    que.append((sy,sx))
    visited[sy][sx] = data[sy][sx]
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx,y,x):
                visited[ny][nx] = visited[y][x] + data[y][x]
                que.append((ny,nx))

M,N = map(int, input().split())
data = [[int(_) for _ in input() ] for _2 in range(N)]
visited = [[0x7ffffff]*M for _ in range(N)]
bfs()
print(visited[N-1][M-1])