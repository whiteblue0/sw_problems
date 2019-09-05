import sys
sys.stdin = open('1219.txt')

def BFS(cx,v):
    que = []
    que.append(cx)
    visited[v] = 1
    while que:
        v = que.pop(0)
        for i in range(1,V+1):
            if G[v][i] and not visited[i]:
                que.append(i)
                visited[i] = 1


T = 10
for tc in range(1,T+1):
    t,E = map(int, input().split())
    temp = list(map(int, input().split()))

    V = 99

    G = [[0]*(V+1) for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(E):
        G[temp[i*2]][temp[i*2+1]] = 1

    # for i in range(E):
    #     print(G[i])


    cx,cy = 0, 99
    result = 0
    BFS(cx,0)
    if visited[cy]:
        result = 1

    print('#{} {}'.format(tc,result))
