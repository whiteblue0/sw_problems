import collections

# 우, 하, 상,좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]
def ispass(y,x,v):
    return 0<=x<N and 0<=y<N and not visited[y][x] and data[y][x] > v

def bfs(sy,sx,v):
    global cnt
    que = collections.deque()
    que.append((sy,sx))
    visited[sy][sx] = cnt
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx,v):
                visited[ny][nx] = cnt
                que.append((ny,nx))
    cnt += 1

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

result = 0
mymax = 0
for i in range(N):
    for j in range(N):
        if data[i][j] > mymax:
            mymax = data[i][j]
mymax += 1
for i in range(mymax):
    visited = [[0]*N for _ in range(N)]
    cnt = 1
    for m in range(N):
        for n in range(N):
            if data[m][n] > i and not visited[m][n]:
                bfs(m,n,i)

    for i in range(N):
        for j in range(N):
            if result < visited[i][j]:
                result = visited[i][j]

print(result)
