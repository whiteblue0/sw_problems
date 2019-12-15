from collections import deque
# 우,하,좌,상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def isapass(y,x):
    return 0<=y<N and 0<=x<N and not visited[y][x]

def bfs(sy,sx):
    global cnt,flag
    que = deque()
    visited[sy][sx] = 1
    que.append((sy,sx))
    people = 0
    people += data[sy][sx]
    nation = [(sy,sx)]
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if isapass(ny,nx) and L<= abs(data[ny][nx]-data[y][x]) <= R:
                flag = 1
                visited[ny][nx] = 1
                people += data[ny][nx]
                nation.append((ny,nx))
                que.append((ny,nx))
    for i in range(len(nation)):
        y = nation[i][0]
        x = nation[i][1]
        data[y][x] = people//len(nation)


N,L,R = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(N)]
union = [0]*(N**2)

cnt = 0

while True:
    flag = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i,j)

    if flag:
        cnt += 1
    else:
        break

print(cnt)