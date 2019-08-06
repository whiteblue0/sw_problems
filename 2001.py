import sys
sys.stdin = open('2001.txt')


T = int(input())
for a in range(1,T+1):
    N, M = map(int, input().split())

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    cnt = 0
    for y in range(N-M+1):
        for x in range(N-M+1):
            temp = 0
            for j in range(M):
                for i in range(M):
                    temp += arr[j+y][i+x]
            if temp > cnt:
                cnt = temp
    print('#{} {}'.format(a, cnt))