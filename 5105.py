import sys
sys.stdin = open('5105.txt')


def ispass(y,x):
    if 0<=y<N and 0<=x<N and visited[y][x] == 0:
        if data[y][x] == 0 or data[y][x] == 3:
            return True
    else:
        return False

def BFS(sy,sx):
    visited[sy][sx] = 1
    que = [(sy,sx)]
    while que:
        y,x = que.pop(0)
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(ny,nx):
                que.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1

# 우하좌상
dy = [0,1,0,-1]
dx = [1,0,-1,0]

T = int(input())

for tc in range(1,T+1):
    N = int(input())


    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                start = (i,j)

    for i in range(N):
        for j in range(N):
            if data[i][j] ==3:
                goal = (i,j)

    BFS(start[0],start[1])

    result = 0
    if visited[goal[0]][goal[1]]:
        result = visited[goal[0]][goal[1]]-2

    # print(visited)

    print('#{} {}'.format(tc,result))