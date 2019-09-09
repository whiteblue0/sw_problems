# 우 하 상 좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def ispass(y,x):
    return 0<=y<N and 0<=x<N

def dfs(sy,sx,string):
    # if string in lst:
    #     return
    if len(string) == 7:
        lst.append(string)
        return

    for d in range(4):
        ny, nx = sy + dy[d], sx + dx[d]
        if ispass(ny, nx):
            dfs(ny,nx,string + data[ny][nx])

T = int(input())
for tc in range(1,T+1):
    N = 4
    data = [input().split() for _ in range(N)]
    lst = []
    visited = [['']*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dfs(i,j,data[i][j])

    result = len(set(lst))
    print("#{} {}".format(tc,result))