from collections import deque

# 우, 하, 좌, 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(y,x):
    return 0<=y<N and 0<=x<N and data[y][x] and not visited[y][x]

def dfs(sy,sx):
    global cnt,lst
    stack = deque()
    visited[sy][sx] = cnt
    stack.append((sy,sx))
    volume = 1
    while stack:
        y,x = stack.pop()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx):
                visited[ny][nx] = cnt
                volume += 1
                stack.append((ny,nx))
    lst.append(volume)
    cnt += 1


N = int(input())
data = []
for i in range(N):
    inp = input()
    temp = []
    for j in inp:
        temp.append(int(j))
    data.append(temp)
visited = [[0]*N for _ in range(N)]
lst = []
cnt = 1

for i in range(N):
    for j in range(N):
        if ispass(i,j):
            dfs(i,j)


lst.sort()
cnt -= 1
print(cnt)
for i in range(len(lst)):
    print(lst[i])