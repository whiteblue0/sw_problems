import sys
sys.stdin = open('1249.txt', 'r')

dx = [0, 0 ,1, -1]
dy = [1, -1, 0, 0]

def ispass(y, x):
    return 0<=x<N and 0<=y<N

def bfs(y,x):

    que = []

    dist[y][x] = 0
    que.append((y, x))

    while len(que) != 0:
        y, x = que.pop(0)

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(ny, nx) and dist[ny][nx] > dist[y][x] + data[ny][nx]:
                dist[ny][nx] =dist[y][x]+data[ny][nx]
                que.append((ny, nx))


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input())) for _ in range(N)]
    dist = [[987654321] * N for _ in range(N)]
    bfs(0,0)
    # for _ in range(N):
    #     print(data[_])
    # print()
    #
    # for _ in range(N):
    #     print(dist[_])
    print("#{} {}".format(tc, dist[N-1][N-1]))
