import sys
sys.stdin = open("2105.txt")
# 우하, 좌하, 좌상, 우상
dx = [1,-1,-1,1]
dy = [1,1,-1,-1]

def ispass(y,x):
    return 0<=x<N and 0<=y<N

def travel(sy,sx):
    global result
    d = 0
    r1 = 0
    r2 = 0
    y,x = sy,sx
    while ispass(y,x):
        y += dy[d]
        x += dx[d]
        r1 += 1
    y -= dy[d]
    x -= dx[d]
    if y == N-1:
        r1 -= 1
        y -= dy[d]
        x -= dx[d]

    d += 1
    while ispass(y,x):
        y += dy[d]
        x += dx[d]
        r2 += 1
    y -= dy[d]
    x -= dx[d]

    for q in range(r1-1):
        t1 = r1 - q
        t2 = r2 + q
        for i in range(t1,1,-1):
            for j in range(t2,1,-1):
                visited = []
                y,x = sy,sx
                visited.append(data[y][x])
                cnt = 1
                d = 0
                while cnt < (i+j)*2-4:
                    ny,nx = y+dy[d],x+dx[d]
                    if not ispass(ny,nx):
                        flag = 0
                        visited = []
                        break
                    if data[ny][nx] in visited:
                        flag = 0
                        visited = []
                        break
                    visited.append(data[ny][nx])
                    cnt += 1
                    if cnt == i or cnt == i+j-1 or cnt == i*2+j-2:
                        d += 1
                        d %= 4
                    y,x = ny,nx
                    flag = 1

                if y-sy != 1 and x-sx != -1:
                    visited = []
                    flag = 0

                if len(visited) > result:
                    result = len(visited)
                if flag:
                    break


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-1):
        for j in range(1,N-1):
            travel(i,j)
    if result == 0:
        result = -1
    print("#%d" % tc,result)