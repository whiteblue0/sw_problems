from collections import deque

def bfs(s):
    que = deque()
    que.append(s)
    visited[s] = 0
    while que:
        f = que.popleft()
        for i in UD:
            if 1<=(f+i)<=F and (visited[f]+1) < visited[f+i]:
                visited[f+i] = visited[f]+1
                que.append(f+i)

# F: 건물 높이
# S: 강호 위치
# G: 스타트링크 위치
# U: 위로 갈수 있는 층수
# D: 아래로 갈수 있는 층수

F,S,G,U,D = map(int,input().split())
visited = [0xfffffff]*(F+1)
UD = [U,-D]
bfs(S)
if visited[G] == 0xfffffff:
    visited[G] = 'use the stairs'
print(visited[G])