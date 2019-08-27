import sys
sys.stdin = open('1226.txt')

def ispass(y,x):
    if 0<=y<L and 0<=x<L and data[y][x] != 1 and visited[y][x] == 0:
        return True
    else:
        return False

def DFS(sy,sx):
    global end
    visited[sy][sx] = 1
    if data[sy][sx] == 3:
        end = 1



    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if ispass(ny, nx):
            visited[ny][nx] = 1
            DFS(ny,nx)

# 우하좌상
dy = [0,1,0,-1]
dx = [1,0,-1,0]

T = 10
for tc in range(1,T+1):
    N = int(input())
    L = 16
    data = [list(map(int, input())) for _ in range(L)]
    visited = [[0]*L for _ in range(L)]

    for i in range(L):
        for j in range(L):
            if data[i][j] == 2:
                start = (i,j)
    end = 0

    DFS(start[0],start[1])

    # for i in range(L):
    #     print(visited[i])

    print('#{} {}'.format(tc,end))