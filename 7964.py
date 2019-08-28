import sys
sys.stdin = open('7964.txt')

T = int(input())
# for i in range(1,T+1):
N,D = map(int, input().split())
lines = list(map(int, input().split()))
node = [[0]*N for _ in range(N)]

# for i in range(N):
#     print(i,node[i])

for i in range(N):
    if lines[i] == 1:
        for j in range(0,D+1):
            if 0<=(i-j)<N :
                node[i][i-j] = 1
            if 0<=(i+j)<N:
                node[i][i+j] = 1

for i in range(N):
    print(i,node[i])