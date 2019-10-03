import collections

def bfs(s):
    que = collections.deque()
    que.append(s)
    visited[s] = 1
    searched.append(s)
    while que:
        c = que.popleft()
        if  not visited[c]:
            visited[c] = 1
            searched.append(c)
        if data[c]:
            for i in range(len(data[c])):
                if not visited[data[c][i]]:
                    que.append(data[c][i])

def dfs(c):
    if  not visited[c]:
        visited[c] = 1
        searched.append(c)
    if data[c]:
        for i in range(len(data[c])):
            if not visited[data[c][i]]:
                dfs(data[c][i])


N, M, V = map(int, input().split())
data = dict()
for i in range(N):
    data[i+1] = []
for _ in range(M):
    s,e = map(int,input().split())
    data[s].append(e)
    data[e].append(s)

for i in range(1,N+1):
    data[i].sort()
visited = [0]*(N+1)
searched = []
dfs(V)
for i in range(len(searched)):
    if i == len(searched)-1:
        print(searched[i])
    else:
        print(searched[i],end=" ")
visited = [0]*(N+1)
searched = []
bfs(V)
for i in range(len(searched)):
    if i == len(searched)-1:
        print(searched[i])
    else:
        print(searched[i],end=" ")

