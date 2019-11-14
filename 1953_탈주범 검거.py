import sys
sys.stdin = open("1953.txt")

import collections
# 우  하  상  좌
# 0   1   2  3
dx = [1,0,0,-1]
dy = [0,1,-1,0]

pipe = {1:[0,1,2,3],
        2:[1,2],
        3:[0,3],
        4:[0,2],
        5:[0,1],
        6:[1,3],
        7:[2,3]}

def ispass(y,x):
    return 0<=y<N and 0<=x<M and not visited[y][x] and data[y][x]

def islink(y,x,dir):
    if dir == 0 and 3 in pipe[data[y][x]]:
        return True
    elif dir == 1 and 2 in pipe[data[y][x]]:
        return True
    elif dir == 2 and 1 in pipe[data[y][x]]:
        return True
    elif dir == 3 and 0 in pipe[data[y][x]]:
        return True
    return False

def bfs(sy,sx):
    global cnt
    que = collections.deque()
    que.append((sy,sx))
    visited[sy][sx] = 1
    cnt = 1
    while que:
        y,x = que.popleft()
        if visited[y][x] == L:
            break
        for i in pipe[data[y][x]]:
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx) and islink(ny,nx,i):
                visited[ny][nx] = visited[y][x] + 1
                cnt += 1
                que.append((ny,nx))

T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    bfs(R,C)
    print("#{} {}".format(tc,cnt))