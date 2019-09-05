import sys
sys.stdin = open("1249.txt")
#   우, 하, 좌, 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(ny,nx):
    return 0<=nx<N and 0<=ny<N

def bfs(s):
    que = []
    visited[s[0]][s[1]] = data[s[0]][s[1]]
    que.append(s)
    while que:
        y,x,k = que.pop(0)
        for i in range(4):
            ny,nx,nk = y+dy[i],x+dx[i],data[y+dy[i]][x+dx[i]]
            if ispass(ny,nx):
                visited[ny][nx] = nk + k




T = int(input())

N = int(input())
data = [[int(_1) for _1 in input()] for _2 in range(N)]
visited = [[0]*N for _ in range(N)]
for _ in range(N):
    print(data[_])

start = (0,0,0)
goal =(N-1,N-1)
