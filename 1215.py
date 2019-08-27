import sys
sys.stdin = open('1215.txt')

T = 10

for tc in range(1,T+1):
    N = int(input())
    table = [input() for k in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            flag = 1
            for k in range(N//2):
                if table[i][j+N-1-k] != table[i][j+k]:
                    flag = 0
                    break
            if flag :
                cnt += 1

    for j in range(8):
        for i in range(8-N+1):
            flag = 1
            for k in range(N//2):
                if table[i+N-1-k][j] != table[i+k][j]:
                    flag = 0
                    break
            if flag :
                cnt += 1

    print('#{} {}'.format(tc, cnt))