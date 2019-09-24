import sys
sys.stdin = open("5250.txt")
import collections

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(y,x):
    return 0<=y<N and 0<=x<N

def bfs(sy,sx):
    que = collections.deque()
    que.append((sy,sx))
    dist[sy][sx] = 0
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx) and data[ny][nx] > data[y][x] and dist[ny][nx] > dist[y][x] + (data[ny][nx]-data[y][x]) + 1:
                dist[ny][nx] = dist[y][x] + (data[ny][nx]-data[y][x]) +1
                que.append((ny,nx))
            elif ispass(ny,nx) and data[ny][nx] <= data[y][x] and dist[ny][nx] > dist[y][x] + 1:
                dist[ny][nx] = dist[y][x] +1
                que.append((ny, nx))


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dist = [[2000*(N**2)]*N for _ in range(N)]
    bfs(0,0)
    # for i in range(N):
    #     print(dist[i])
    print("#{} {}".format(tc,dist[-1][-1]))