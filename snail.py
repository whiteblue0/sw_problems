import sys
sys.stdin = open("input.txt")

def ispass(y,x):
    return 0<=y<N and 0<=x<N and not data[y][x]

N = int(input())
data = [[0]*N for _ in range(N)]

# 우,하,좌,상,
dy = [0,1,0,-1]
dx = [1,0,-1,0]

# 우하, 좌상, 우상, 우하
# dy = [1,-1,-1,1]
# dx = [1,-1,1,-1]

y,x,d = 0,0,0

for i in range(N**2):
    data[y][x] = i+1
    ny,nx = y+dy[d], x+dx[d]
    if not ispass(ny,nx):
        d += 1
        d %= 4
        ny,nx=y+dy[d],x+dx[d]
    y,x = ny,nx

