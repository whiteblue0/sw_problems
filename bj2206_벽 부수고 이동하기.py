from collections import deque

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
dist = [[[0, 0] for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1
    while q:
        y, x, w = q.popleft()
        if y == N-1 and x == M-1:
            return dist[y][x][w]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if dist[ny][nx][w]:
                continue
            if data[ny][nx] == '0':
                dist[ny][nx][w] = dist[y][x][w] + 1
                q.append((ny, nx, w))
            if data[ny][nx] == '1' and w == 0:
                dist[ny][nx][1] = dist[y][x][w] + 1
                q.append((ny, nx, 1))
    return -1

print(bfs())