import sys
sys.stdin = open('4881.txt')

def DFS(c,cnt):
    global myMin
    if c == N:
        if myMin > cnt:
            myMin = cnt
        return
    if cnt > myMin:
        return
    for i in range(N):
        if not visited[i]:
            cnt += data[c][i]
            visited[i] = 1
            DFS(c+1,cnt)
            cnt -= data[c][i]
            visited[i]=0

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int, input().split()))for _ in range(N)]
    visited = [0]*N
    myMin=987654321
    DFS(0, 0)
    print('#{} {}'.format(tc+1,myMin))