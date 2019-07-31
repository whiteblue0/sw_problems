import sys
sys.stdin = open('1986.txt')

T = int(input())

for k in range(1,T+1):
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        if i%2:
            cnt += i
        else:
            cnt -= i

    print('#{} {}'.format(k,cnt))