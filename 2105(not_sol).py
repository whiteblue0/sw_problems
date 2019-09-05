import sys
sys.stdin = open("2105.txt")
# 우하, 좌하, 좌상, 우상
dx = [1,-1,-1,1]
dy = [1,1,-1,-1]

def ispass(ny,nx,y,x):
    if 0<=nx<N and 0<=ny<N and visited[ny][nx] >= visited[y][x]  and  not data[ny][nx] in ate:
        return True
    else:
        return False

def dfs(sy,sx):
    global ate
    stack = []
    ate = []
    ate.append(data[sy][sx])
    stack.append((sy,sx))
    visited[sy][sx] = 1
    data[sy][sx] = 0
    cnt = 0
    while stack:

        y,x = stack.pop()
        print(y,x)
        for d in range(4):

            ny,nx = y+dy[d],x+dx[d]
            print("ny,nx",ny,nx)
            if ispass(ny,nx,y,x):
                visited[ny][nx] = visited[y][x] + 1
                if ny == sy and nx == sx and y != sy and x != sx:
                    if cnt <= len(ate):
                        cnt = len(ate)
                    continue
                stack.append((ny,nx))
                ate.append(data[ny][nx])
                print(stack)
    # print(ate)






T = int(input())
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited[0][0] = 999
visited[0][N-1] = 999
visited[N-1][0] = 999
visited[N-1][N-1] = 999
# for _ in range(N):
#     print(data[_])
#     print(visited[_])

for i in range(N):
    for j in range(N):
        if visited[i][j] != 999:
            dfs(i,j)