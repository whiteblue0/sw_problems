import sys
from copy import deepcopy
sys.stdin = open('1949.txt')

# 우 하 상 좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def ispass(ny,nx,y,x):
    return 0 <= nx < N and 0 <= ny < N and visited[ny][nx] < visited[y][x] and data[ny][nx] < data[y][x]

def dfs(sy,sx):
    global data
    stack = []
    visited[sy][sx] = 1
    stack.append((sy,sx))
    while stack:
        y,x = stack.pop()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]

            if ispass(ny,nx,y,x):
                visited[ny][nx] = visited[y][x] + 1

                stack.append((ny,nx))




T = int(input())
for tc in range(1,T+1):
    N,K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    # for _ in range(N):
    #     print(mountain[_])

    top = 1
    bottom = 20
    for _1 in range(N):
        for _2 in range(N):
            if mountain[_1][_2] > top:
                top = mountain[_1][_2]
            if mountain[_1][_2] < bottom:
                bottom = mountain[_1][_2]


    line = 0
    for i in range(N):
        for j in range(N):
            for k in range(1,K+1):
                data = deepcopy(mountain)
                visited = [[0] * N for _ in range(N)]
                data[i][j] -= k
                for n in range(N):
                    for m in range(N):
                        if data[n][m] == top:
                            dfs(n,m)
                for b in range(N):
                    for a in range(N):
                        if line < visited[b][a]:
                            line = visited[b][a]

                print("깊이:{},좌표:{},{}".format(k,n,m))
                for _ in range(N):
                    print(data[_])
                print()

                for _ in range(N):
                    print(visited[_])
                print()


    print("#{} {}".format(tc,line))