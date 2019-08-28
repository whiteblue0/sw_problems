import sys
sys.stdin = open('그래프 경로.txt')

T = int(input())


def DFS(n):
    global result
    visited[n] = 1
    if cy == n:
        result = 1

    for i in range(V + 1):
        if G[n][i] == 1 and visited[i] == 0:
            DFS(i)

for tc in range(1,T+1):
    V, E = map(int, input().split())
    temp = []
    for i in range(E):
        start,end = map(int, input().split())
        temp.append(start)
        temp.append(end)

    cx,cy = map(int, input().split())
    check = (cx,cy)

    stack = []


    G = [[0 for _ in range(V+1)] for a in range(V+1)]
    visited = [0 for i in range(V+1)]

    for i in range(0, len(temp),2):
        G[temp[i]][temp[i+1]] = 1

    # for i in range(V+1):
    #     print('{} {}'.format(i,G[i]))

    result = 0
    DFS(cx)

    if result:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))

