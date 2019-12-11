from copy import deepcopy

def ispass(y,x):
    return 0<=y<N and 0<=x<M and not data[y][x] == 6

# 우 하 좌 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

view = {
    1:[[0],[1],[2],[3]],
    2:[[0,2],[1,3]],
    3:[[0,1],[1,2],[2,3],[3,0]],
    4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5:[[0,1,2,3]]
}

def getsecure(lst):
    scope = deepcopy(data)
    for i in range(len(cam)):
        for j in range(len(lst[i])):
            y = cam[i][0]
            x = cam[i][1]
            d = lst[i][j]
            while ispass(y,x):
                ny,nx = y + dy[d], x + dx[d]
                if ispass(ny,nx):
                    if scope[ny][nx] == 0:
                        scope[ny][nx] = 9
                    y,x = ny,nx
                y,x = ny,nx

    cnt = 0
    for i in range(N):
        for j in range(M):
            if scope[i][j] == 0:
                cnt += 1
    return cnt

def dfs(c):
    global result
    if c == K:
        cnt = getsecure(camdir)
        if result > cnt:
            result = cnt
        return


    for i in range(len(view[cam[c][2]])):
        camdir[c] = view[cam[c][2]][i]
        dfs(c+1)


N,M = map(int,input().split())
data = [list(map(int, input().split())) for _ in range(N)]

cam = []
K = 0
result = 0xfffffff

for i in range(N):
    for j in range(M):
        if data[i][j] and data[i][j] != 6:
            cam.append([i,j,data[i][j]])
            K += 1

visited = [0]*K
camdir = [0]*K

dfs(0)
print(result)