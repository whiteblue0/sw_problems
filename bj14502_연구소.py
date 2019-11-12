from collections import deque
import itertools
from copy import deepcopy

#우, 하, 상 ,좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def ispass (y,x):
    return 0<=y<N and 0<=x<M and not tempdata[y][x] and not visited[y][x]

def BFS(sy,sx):
    que = deque()
    que.append((sy,sx))
    visited[q][w] = 1
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx):
                visited[ny][nx] = 1
                tempdata[ny][nx] = 2
                que.append((ny,nx))

N,M = map(int,input().split())
data = [list(map(int, input().split())) for _ in range(N)]
l = []

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            l.append((i,j))
wall = list(itertools.combinations(l,3))

result = 0
for i in range(len(wall)):

    tempdata = deepcopy(data)
    visited = [[0] * M for _ in range(N)]

    for j in range(3):
        y = wall[i][j][0]
        x = wall[i][j][1]
        tempdata[y][x] = 3
    for q in range(N):
        for w in range(M):
            if tempdata[q][w] == 2 and not visited[q][w]:
                BFS(q,w)

    cnt = 0
    for c1 in range(N):
        for c2 in range(M):
            if tempdata[c1][c2] == 0:
                cnt += 1
    if cnt > result:
        result = cnt
print(result)