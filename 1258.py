import sys
sys.stdin = open('1258.txt')

# 우 하 좌 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(y,x):
    return 0<=y<N and 0<=x<N and data[y][x] and visited[y][x] == 0

def BFS(sy,sx):
    global info
    que = []
    que.append((sy,sx))
    visited[sy][sx] = cnt

    ymin, ymax = sy, sx
    xmin, xmax = sy, sx

    while que:
        y,x = que.pop(0)
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(ny,nx):
                que.append((ny,nx))
                visited[ny][nx] = cnt
                if ny <= ymin:
                    ymin = ny
                if ny >= ymax:
                    ymax = ny
                if nx <= xmin:
                    xmin = nx
                if nx >= xmax:
                    xmax = nx
    print(ymax+1,ymin,xmax+1,xmin)
    info.append(((ymax-ymin+1),(xmax-xmin+1)))



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))


    visited = [[0]*N for n in range(N)]
    info = []
    cnt = 1
    for i in range(N):
        for j in range(N):
            if ispass(i,j):
                BFS(i,j)
                cnt += 1

    cnt -= 1


    #   Bubblesort
    for i in range(len(info)-1,0,-1):
        for j in range(0,i):
            if info[j][0]*info[j][1] > info[j+1][0]*info[j+1][1]:
                info[j], info[j+1] = info[j+1], info[j]
    for i in range(len(info)-1,0,-1):
        for j in range(0, i):
            if info[j][0]*info[j][1] == info[j+1][0]*info[j+1][1]:
                if info[j][0] > info[j+1][0]:
                    info[j], info[j+1] = info[j+1], info[j]


    print(info)
    # print('#{} {}'.format(tc,cnt),end=' ')
    # for i in range(len(info)):
    #     print(info[i][0],info[i][1],end=' ')
    # print()