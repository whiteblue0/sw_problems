import sys
sys.stdin = open('2805.txt')

# 우 하 상 좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def ispass(y,x):
    return 0<=x<N and 0<=y<N and not visited[y][x]

def bfs(sy,sx):
    que =[]
    visited[sy][sx] = 1
    que.append((sy,sx))
    while que:
        y,x = que.pop(0)
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx):
                visited[ny][nx] = visited[y][x] + 1
                if visited[ny][nx] == N//2+1:
                    continue
                que.append((ny,nx))



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [[int(_) for _ in input()] for _2 in range(N)]
    visited = [[0]*N for _ in range(N)]
    # for _ in range(N):
    #     print(data[_])

    sy,sx = N//2, N//2
    bfs(sy,sx)

    result = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                result += data[i][j]
    print("#{} {}".format(tc, result))
