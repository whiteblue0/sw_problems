import sys
sys.stdin = open('4615.txt')

# 상 우상 우 우하 하 좌하 좌 좌상
dx = [ 0, 1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1, 1, 0,-1]

def ispass(x,y):
    return 0<=x<N and 0<=y<N


def turnover(x,y,c):
    if c == 1:
        ec = 2
    else:
        ec = 1

    table[y][x] = c
    # print('x,y',x,y,end=' ')
    for i in range(8):
        nx,ny = x+dx[i],y+dy[i]
        if ispass(nx,ny) and table[ny][nx] == ec:
            cy,cx = ny+dy[i],nx+dx[i]
            if ispass(cx,cy):
                cnt = 0
                while table[cy][cx] == c:
                    cy += dy[i]
                    cx += dx[i]
                    cnt += 1
                    if not ispass(cx,cy):
                        break
                    elif table[cy][cx] == 0:
                        break
                print('dir', i)
                print('cx,cy',cx,cy)
                print('#{} x,y'.format(r),x,y)

                if table[cy-dy[i]][cx-dx[i]] == c:
                    cy -= dy[i]
                    cx -= dx[i]
                    print('cnt',cnt)
                    for u in range(1,cnt+1):
                        table[cy][cx] = c
                        cy -= dy[i]
                        cx -= dx[i]

                for _ in range(N):
                    print(table[_])


T = int(input())

N,M = map(int, input().split())
table = [[0]*N for _ in range(N)]

middle = N//2
table[middle][middle] = 2
table[middle-1][middle] = 1
table[middle][middle-1] = 1
table[middle-1][middle-1] = 2


# for i in range(N):
#     print(table[i])

# place[0] = x, place[1] = y, place[3] = color
for r in range(M):
    point = (list(map(int, input().split())))
    point[0] -= 1
    point[1] -= 1
    x,y,c = point[0], point[1], point[2]
    turnover(x,y,c)

