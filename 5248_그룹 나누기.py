import sys
sys.stdin = open('5248.txt')

def findSet(x):
    if x == P[x]:
        return x
    else:
        return findSet(P[x])

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    P = list(range(N + 1))
    for i in range(M):
        a = data[2 * i]
        b = data[2 * i + 1]
        P[findSet(b)] = findSet(a)  # b의 대표 원소를 a의 대표원소로 교체

    cnt = 0;
    for i in range(1, N + 1):  # 대표원소가 자기 자신인 경우의 수
        if P[i] == i:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
