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

            while table[ny][nx] == ec:
                ny += dy[i]
                nx += dx[i]
                if not ispass(nx,ny):
                    ny -= dy[i]
                    nx -= dx[i]
                    break

            if table[ny][nx] == c:
                while ny != y or nx != x:
                    table[ny][nx] = c
                    ny -= dy[i]
                    nx -= dx[i]


            # for _ in range(N):
            #     print(table[_])


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    table = [[0]*N for _ in range(N)]

    middle = N//2
    table[middle][middle] = 2
    table[middle-1][middle] = 1
    table[middle][middle-1] = 1
    table[middle-1][middle-1] = 2


    # for i in rangee[i])

    # place[0] = x, place[1] = y, place[3] = color
    for r in range(M):
        point = (list(map(int, input().split())))
        point[0] -= 1
        point[1] -= 1
        x,y,c = point[0], point[1], point[2]
        turnover(x,y,c)

    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                cnt1+=1
            elif table[i][j] ==2:
                cnt2+=1
    print("#{} {} {}".format(tc,cnt1,cnt2))

