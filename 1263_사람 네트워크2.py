import sys
sys.stdin = open("1263.txt")
import collections

def bfs(c):
    que = collections.deque()
    que.append(c)
    visited[c] = 0
    cnt = 0
    while que:
        t = que.popleft()
        for i in range(N):
            if t != i and table[t][i] and visited[i] > table[t][i] + visited[t]:
                visited[i] = table[t][i] + visited[t]
                cnt += visited[i]
                que.append(i)

def bfs2(c):
    global result
    que = collections.deque()
    que.append(c)
    visited[c] = 0
    cnt = 0
    while que:
        if cnt > result:
            break
        t = que.popleft()
        for i in range(N):
            if t != i and table[t][i] and visited[i] > table[t][i] + visited[t]:
                visited[i] = table[t][i] + visited[t]
                cnt += visited[i]
                que.append(i)
    if result > cnt:
        result = cnt

T = int(input())
for tc in range(1,T+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    table = [[0]*N for _ in range(N)]
    visited = [0x7ffffff] * N
    for i in range(N):
        for j in range(N):
            table[i][j] = temp[1+i*N+j]
    result = 0x7ffffff
    # [print(table[i]) for i in range(N)]

    bfs(0)
    result = sum(visited)
    for i in range(1,N):
        visited = [0x7ffffff] * N
        bfs2(i)
        # print(visited)

    print("#{} {}".format(tc,result))