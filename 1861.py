# 우,하,좌,상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(y,x):
    return 0<=y<N and 0<=x<N

def findpath(sy,sx):
    global result

    que =[]
    cnt = 1
    # visited[sy][sx] = 1
    que.append((sy,sx))
    while que:
        y,x = que.pop(0)
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if ispass(ny,nx) and (data[ny][nx] == data[y][x]+1):
                cnt += 1
                que.append((ny,nx))

    if cnt >= result[1]:
        result[1] = cnt
        result[0] = data[sy][sx]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    nums = [0]*(N**2+1)
    result = [N**2, 0]

    for i in range(N):
        for j in range(N):
            nums[data[i][j]] = (i,j)

    for i in range(N**2,0,-1):
        sy,sx = nums[i][0], nums[i][1]
        findpath(sy,sx)
    print("#{}".format(tc),result[0],result[1])
