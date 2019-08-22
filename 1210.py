import sys
sys.stdin = open("1210.txt")

T = 10

for tc in range(10):
    N=int(input())
    l=100
    data = [list(map(int, input().split())) for _ in range(l)]


    #좌,우,상
    dx = [-1,1,0]
    dy = [0,0,-1]

    def ispass(y,x):
        return 0<=x<l and 0<=y<l and data[y][x]

    for i in range(l):
        if data[99][i] == 2:
            y, x = (99, i)
            start = x
            # print('start:({},{})'.format(x,y))
            d = 0

            while y > 0:
                ny, nx = y+dy[d], x+dx[d]
                if d == 0 or d == 1:
                    if ispass(ny, nx):
                        y, x = ny, nx
                    else:
                        d = 2
                else:
                    if ispass(ny, nx):
                        y, x = ny, nx
                        for a in range(2):
                            d += 1
                            d %= 3
                            ay,ax=y+dy[d],x+dx[d]
                            if ispass(ay, ax):
                                break



                # print('d:{} x:{} y:{}'.format(d,x,y))
            # if data[y][x] == 2:
            print('#{} {}'.format(tc+1,x))


