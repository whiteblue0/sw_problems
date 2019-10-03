import itertools
N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
cnt = 3
l = []
blocked = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            l.append((i,j))
wall = list(itertools.combinations(l,3))
print(wall)
print(len(wall))