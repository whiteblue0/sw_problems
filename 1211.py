import sys
sys.stdin = open("1210.txt")

T = 10

for tc in range(10):

    N=int(input())
    l=100
    data = [list(map(int, input().split())) for _ in range(l)]


    #좌,우,하
    dx = [-1,1,0]
    dy = [0,0,1]


    def ispass(y,x):
        return 0<=x<l and 0<=y<l and data[y][x]
    minlength = 100**2

    for i in range(l):

        if data[0][i] == 1:
            y, x = (0, i)
            start = x
            # print('start:({},{})'.format(x,y))
            d = 0
            cnt=0

            while y < l-1:
                ny, nx = y+dy[d], x+dx[d]
                if d == 0 or d == 1:
                    if ispass(ny, nx):
                        y, x = ny, nx
                        cnt += 1
                    else:
                        d = 2
                else:
                    if ispass(ny, nx):
                        y, x = ny, nx
                        cnt += 1
                        for a in range(2):
                            d += 1
                            d %= 3
                            ay,ax=y+dy[d],x+dx[d]
                            if ispass(ay, ax):
                                break
            if minlength >= cnt:
                minlength = cnt
                ans = start
                # print('d:{} x:{} y:{}'.format(d,x,y))
    # print('#{} start:{} x,y: {},{} length: {}'.format(tc+1,ans,x,y,minlength))
    print('#{} {}'.format(tc+1,ans))
