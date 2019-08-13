import sys
sys.stdin = open('4836.txt')

T = int(input())

for a in range(1,T+1):
    N = int(input())
    table = [[0]*10 for _ in range(10)]
    base = []
    for i in range(N):
        base.append(list(map(int, input().split())))

    # print(base)

    for n in range(len(base)):
        if base[n][-1] == 1:
            for j in range(base[n][1],base[n][3]+1):
                for i in range(base[n][0],base[n][2]+1):
                    table[j][i] = 1

    for n in range(len(base)):
        if base[n][-1] == 2:
            for j in range(base[n][1],base[n][3]+1):
                for i in range(base[n][0],base[n][2]+1):
                    if table[j][i] == 1:
                        table[j][i] = 2


    cnt = 0
    for y in range(10):
        for x in range(10):
            if table[y][x] ==2:
                cnt += 1

    print('#{} {}'.format(a, cnt))