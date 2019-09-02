import sys
sys.stdin = open('1227.txt')

#   우 하 상 좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def ispass(y,x):
    return 0<=x<N and 0<=y<N and not visited[y][x] and data[y][x] != 1

def BFS(sy,sx):
    visited[sy][sx] = 1
    que = []
    que.append((sy,sx))
    while que:
        y,x = que.pop(0)
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if ispass(ny,nx):
                que.append((ny,nx))
                visited[ny][nx] = 1

T = 10
for tc in range(1,T+1):
    t = int(input())
    N = 100
    data = [list(map(int, input())) for _ in range(N)]
    result = 0

    visited = [[0]*N for _ in range(N)]

    # for i in range(N):
    #     print(data[i])

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                sy, sx = i, j

    BFS(sy,sx)
    for i in range(N):
        for j in range(N):
            if data[i][j] == 3 and visited[i][j] == 1:
                result = 1



    print('#{} {}'.format(tc, result))
