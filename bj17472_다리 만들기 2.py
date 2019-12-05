from collections import deque

# 우 하 상 좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def iswater(y,x):
    return 0<=y<N and 0<=x<M and data[y][x] == 0

def isIsle(y,x):
    return 0 <= y < N and 0 <= x < M and data[y][x] and not isleMap[y][x]

def isIsleMap(y,x):
    return 0 <= y < N and 0 <= x < M and isleMap[y][x]

def checkBridge(y,x):
    islenum = isleMap[y][x]
    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if iswater(ny,nx) and iswater(ny+dy[i],nx+dx[i]):
            Blen = 2
            ny2,nx2 = ny+dy[i],nx+dx[i]
            while 0<=ny2<N and 0<=nx2<M:
                # if isleMap[ny2][nx2]>0 and bridge[islenum-1][isleMap[ny2][nx2]-1] > Blen:
                #     bridge[islenum-1][isleMap[ny2][nx2]-1] = Blen - 1
                #     break
                if isleMap[ny2][nx2]>0:
                    for k in range(len(edge)):
                        if edge[k][0] != islenum and edge[k][1] != isleMap[ny2][nx2]:
                            if edge[k][1] != islenum and edge[k][0] != isleMap[ny2][nx2]:
                                edge.append([islenum-1, isleMap[ny2][nx2]-1, Blen])
                        if edge[k][0] == islenum and edge[k][1] == isleMap[ny2][nx2] and edge[k][2] > Blen:
                            edge[k][2] = Blen
                ny2+=dy[i]
                nx2+=dx[i]
                Blen+=1

def makeEdge():
    for i in range(cntisl):
        for j in range(cntisl):
            if i != j:
                for k in range(len(edge)):
                    if edge[k][0] == i and edge[k][1] == j:
                        if edge[k][2] > bridge[i][j]:
                            edge[k][2] = bridge[i][j]
                    elif edge[k][0] == j and edge[k][1] == i:
                        if edge[k][2] > bridge[i][j]:
                            edge[k][2]=bridge[i][j]
                edge.append([i,j,bridge[i][j]])



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

bridge = [[99]*(cntisl) for _ in range(cntisl)]
edge = []


for i in range(N):
    for j in range(M):
        if isleMap[i][j]:
            checkBridge(i,j)

for i in range(N):
    print(isleMap[i])
print()

for i in range(len(edge)):
    print(i,edge[i])

