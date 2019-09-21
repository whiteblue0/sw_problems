import collections

def bfs(s):
    que = collections.deque()
    que.append(s)
    visited[s] = 1
    searched.append(s)
    while que:
        c = que.popleft()
        if data[c]:
            for i in range(len(data[c])):
                if not visited[data[c][i]]:
                    que.append(data[c][i])
                    visited[data[c][i]] = 1
                    searched.append(data[c][i])

def dfs(s):
    stack = collections.deque()
    stack.append(s)
    while stack:
        c = stack.pop()
        if not visited[c] and data[c]:
            visited[c] = 1
            searched.append(c)

            for i in range(len(data[c])-1,-1,-1):
                if not visited[data[c][i]]:
                    stack.append(data[c][i])


N, M, V = map(int, input().split())
data = dict()
for i in range(N):
    data[i+1] = []
for _ in range(M):
    s,e = map(int,input().split())
    data[s].append(e)
    data[e].append(s)

for i in range(1,N+1):
    data[i] = data[i].sort()

visited = [0]*(N+1)
searched = []
bfs(V)
print(searched)

visited = [0]*(N+1)
searched = []
dfs(V)
# print(searched)
for i in range(len(searched)):
    if i == len(searched)-1:
        print(searched[i])
    else:
        print(searched[i],end=" ")

