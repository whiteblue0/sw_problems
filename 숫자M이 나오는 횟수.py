import sys
sys.stdin = open('숫자M.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    cnt = 0
    for i in range(1,N+1):
        l = len(str(i))
        for j in range(l):
            if i%10 == M:
                cnt += 1
            i //= 10


    print('#{} {}'.format(tc, cnt))