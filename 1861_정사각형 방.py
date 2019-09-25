import sys
sys.stdin = open("1861.txt")
import collections

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def ispass(ny,nx,y,x):
    return 0<=ny<N and 0<=nx<N and data[ny][nx] == data[y][x] + 1

def bfs(sy,sx):
    global dist,cnt
    que = collections.deque()
    que.append((sy,sx))
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx,y,x):
                cnt += 1
                if dist <= cnt:
                    dist = cnt
                    trial.append([data[sy][sx],dist])
                que.append((ny,nx))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dist = 0
    trial = []
    for i in range(N):
        for j in range(N):
            cnt = 1
            bfs(i,j)
    trial.sort()
    result = N**2
    for i in range(len(trial)):
        if trial[i][1] == dist:
            if result > trial[i][0]:
                result = trial[i][0]

    print("#{} {} {}".format(tc,result,dist))