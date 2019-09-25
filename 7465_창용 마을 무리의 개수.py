import sys
sys.stdin = open('7465.txt')

def findSet(x):
    if x == P[x]:
        return x
    else:
        return findSet(P[x])

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    P = list(range(N + 1))
    for i in range(M):
        data = list(map(int, input().split()))
        a = data[0]
        b = data[1]
        P[findSet(b)] = findSet(a)

    cnt = 0;
    for i in range(1, N + 1):
        if P[i] == i:
            cnt += 1
    print('#{} {}'.format(tc, cnt))