import sys
sys.stdin = open('1979.txt')


T = int(input())

for a in range(T):
    arr = []
    N, K = map(int, input().split())
    for i in range(N):
        arr.append(list(map(int, input().split())))

    fit = 0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if cnt == K:
                    if i == N-1:
                        fit += 1
                        cnt = 0
                    elif arr[j][i+1] == 0:
                        fit += 1
                        cnt = 0
                elif cnt > K:
                    cnt = 0
            else:
                cnt = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if cnt == K:
                    if j == N-1:
                        fit += 1
                        cnt = 0
                    elif arr[j+1][i] == 0:
                        fit += 1
                        cnt = 0
                elif cnt > K:
                    cnt = 0
            else:
                cnt = 0

    print('#{} {}'.format(a+1, fit))

