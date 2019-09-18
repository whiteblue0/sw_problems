import sys
sys.stdin = open("5188.txt")

#우 하
dx = [1,0]
dy = [0,1]

def ispass(y,x):
    return 0<=y<N and 0<=x<N

def bfs(y,x):
    que = []
    dist[y][x] = data[0][0]
    que.append((y,x))

    while que:
        y,x = que.pop(0)

        for i in range(2):
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(ny,nx) and dist[ny][nx] > dist[y][x]+ data[ny][nx]:
                dist[ny][nx] = dist[y][x] + data[ny][nx]
                que.append((ny,nx))

    pass

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dist = [[987654321]*N for _ in range(N)]

    bfs(0,0)
    result = dist[-1][-1]

    print("#{} {}".format(tc,result))

