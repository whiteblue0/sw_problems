# 우,하,좌,상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(y,x):
    return 0<=y<N and 0<=x<M and data[y][x]==0

def tilt(d,sry,srx,sby,sbx):
    flag = 0
    isred = 0
    isblue = 0
    ry,rx,by,bx = sry,srx,sby,sbx
    while True:
        nby,nbx = by+dy[d],bx+dx[d]
        if [nby,nbx] == hole:
            flag = -1
            return (ry,rx,by,bx,flag)
        elif [nby, nbx] == [sry,srx]:
            isred = 1
        elif data[nby][nbx] == 9:
            nby -= dy[d]
            nbx -= dx[d]
            by, bx = nby, nbx
            break
        by,bx = nby,nbx
    if isred:
        by -= dy[d]
        bx -= dx[d]

    if not flag:
        while True:
            nry,nrx = ry+dy[d],rx+dx[d]
            if [nry,nrx] == hole and not flag == -1:
                ry, rx = nry, nrx
                flag = 1
                break
            elif [nry, nrx] == [sby,sbx]:
                isblue = 1
            elif data[nry][nrx] == 9:
                nry -= dy[d]
                nrx -= dx[d]
                ry, rx = nry, nrx
                break
            ry,rx = nry,nrx
        if isblue:
            ry -= dy[d]
            rx -= dx[d]

    return (ry,rx,by,bx,flag)

def dfs(d,ry,rx,by,bx,cnt):
    global ans
    cnt += 1
    (ry,rx,by,bx,flag) = tilt(d,ry,rx,by,bx)

    if flag == -1 and not ans > 0:
        ans = flag
        return
    elif flag == 1:
        if ans == 0 or ans == -1:
            ans = cnt
        elif cnt < ans:
            ans = cnt
        return
    elif cnt == 10:
        return

    for i in range(4):
        if i != d and not visited[cnt]:
            visited[cnt] = 1
            dfs(i,ry,rx,by,bx,cnt)
            visited[cnt] = 0


N,M = map(int, input().split())
data = [[0]*M for _ in range(N)]
for i in range(N):
    temp = input()
    for j in range(M):
        if temp[j] == '#':
            data[i][j] = 9
        elif temp[j] == '.':
            data[i][j] = 0
        elif temp[j] == 'B':
            data[i][j] = 0
            blue = [i,j]
        elif temp[j] == 'R':
            data[i][j] = 0
            red = [i,j]
        elif temp[j] == 'O':
            data[i][j] = -1
            hole = [i,j]

ans = 0
visited = [0]*11
for i in range(4):
    dfs(i,red[0],red[1],blue[0],blue[1],0)

if ans == 0:
    ans = -1
print(ans)

# testCase
10 10
##########
#RB....#.#
#..#.....#
#........#
#.O......#
#...#....#
#........#
#........#
#.......##
##########

output: 10