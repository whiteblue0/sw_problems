import collections

def ispass(y):
    return 0<=y<N


# def dfs(y,x,cnt):
#     global result
#
#     if y == N-1:
#         if result < cnt:
#             result = cnt
#         return
#
#     elif y == 0:
#         cnt += data[y][x]
#         visited[y][x] = cnt
#
#     for i in range(2):
#         ny,nx = y+1,x+i
#         if ispass(ny):
#             if visited[ny][nx] < cnt + data[ny][nx]:
#                 visited[ny][nx] = cnt + data[ny][nx]
#                 dfs(ny,nx,visited[ny][nx])

def bfs(sy,sx,cnt):
    que = collections.deque()
    que.append((sy,sx))
    visited[sy][sx] = data[sy][sx]
    cnt += visited[sy][sx]
    while que:
        y,x = que.popleft()
        for i in range(2):
            ny,nx  = y+1,x+i
            if ispass(ny):
                if visited[ny][nx] < visited[y][x] + data[ny][nx]:
                    visited[ny][nx] = visited[y][x] + data[ny][nx]
                    que.append((ny,nx))

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]* i for i in range(1,N+1)]
result = 0
# for i in range(N):
#     print(data[i])
#

bfs(0,0,0)
result = max(visited[-1])
print(result)
# for i in range(N):
#     print(visited[i])