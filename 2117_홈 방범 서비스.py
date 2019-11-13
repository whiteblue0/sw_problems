import sys
sys.stdin = open("2117.txt")
from collections import deque

# 우,하,상,좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def isbenefit(house,cost):
    return bool((house*M - cost)>=0)

def ispass(y,x):
    return 0<=x<N and 0<=y<N and not visited[y][x]


def bfs(sy,sx,K):
    global result
    house = 0
    que = deque()
    que.append((sy,sx))
    visited[sy][sx] = 1
    if data[sy][sx]:
        house += 1

    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if ispass(ny,nx) and visited[y][x] < K:
                visited[ny][nx] = visited[y][x] + 1
                if data[ny][nx]:
                    house += 1
                que.append((ny,nx))

    cost =  K*K + (K - 1)*(K - 1)
    if isbenefit(house,cost) and house > result:
        result = house


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            for k in range(1,N+3):
                visited = [[0] * N for _ in range(N)]
                bfs(i,j,k)
                # for _ in range(N):
                #     print(visited[_])
                # print()
    print("#{} {}".format(tc,result))


