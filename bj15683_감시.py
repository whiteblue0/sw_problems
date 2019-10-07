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

def dfs(sy,sx):
    pass


N,M = map(int,input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cam = dict()
for _ in range(1,6):
    cam[_] = []
outrange = 0
for i in range(N):
    for j in range(M):
        if data[i][j] and data[i][j] != 6:
            cam[data[i][j]].append((i,j))
        elif data[i][j] == 0:
            outrange += 1

print(cam)
for i in range(1,6):
    if cam[i]:
        dfs(cam[i][0])
        break