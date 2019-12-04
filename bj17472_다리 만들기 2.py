from collections import deque

# 우 하 상 좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def iswater(y,x):
    return 0<=y<N and 0<=x<M and data[y][x] == 0

def isIsle(y,x):
    return 0 <= y < N and 0 <= x < M and data[y][x] and not isleMap[y][x]

def checkBridge(y,x):
    global cntB
    islenum = isleMap[y][x]
    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if iswater(ny,nx) and iswater(ny+dy[i],nx+dx[i]):
            cntB = 2
            ny2,nx2 = ny+dy[i],nx+dx[i]
            while 0<=ny2<N and 0<=nx2<M:
                ny2 += dy[i]
                nx2 += dx[i]
                cntB += 1
                if isIsle(ny2,nx2) and bridge[islenum][isleMap[ny2][nx2]] > cntB:
                    bridge[islenum][isleMap[ny2][nx2]] = cntB-1
                    break



def makeisle(sy,sx):
    que = deque()
    isleMap[sy][sx] = cntisl
    que.append((sy,sx))
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if isIsle(ny,nx):
                isleMap[ny][nx] = cntisl
                que.append((ny,nx))


N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
isleMap = [[0]*M for _ in range(N)]

cntisl = 0
for i in range(N):
    for j in range(M):
        if data[i][j] and not isleMap[i][j]:
            cntisl += 1
            makeisle(i,j)

bridge = [[9]*(cntisl+1) for _ in range(cntisl+1)]


for i in range(N):
    for j in range(M):
        if isleMap[i][j]:
            checkBridge(i,j)

for i in range(N):
    print(isleMap[i])
print()

for i in range(len(bridge)):
    print(bridge[i])

# for i in range(N):
#     print(isleMap[i])