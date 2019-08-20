

def ispass(y,x):
    if 0<=y<N and 0<=x<N and data[y][x] == 0 and visited[y][x] == 0:
        return True
    else:
        return False

def BFS(sy,sx):
    visited[sy][sx] = 1
    que = [(sy,sx)]
    cnt = 0
    while que:

        y,x = que.pop(0)
        if data[y][x]==3:
            break
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(ny,nx):
                que.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1
                cnt += 1



# 우하좌상
dy = [0,1,0,-1]
dx = [1,0,-1,0]

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

for j in range(N):
    for i in range(N):
        if data[j][i] == 2:
            start = (i,j)
BFS(start)

print(visited[N-1][N-1])
