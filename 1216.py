import sys
sys.stdin = open('1216.txt')

T = 10

for tc in range(1,T+1):
    N = int(input())
    table = [input() for _ in range(100)]

    lmax = 0
    for i in range(100):
        for l in range(100):
            for j in range(100-l+1):
                flag = 1
                for k in range(l // 2):
                    if table[i][j+l-1-k] != table[i][j + k]:
                        flag = 0
                        break
                if flag:
                    if lmax <= l:
                        lmax = l


    for j in range(100):
        for l in range(100):
            for i in range(100-l+1):
                flag = 1
                for k in range(l // 2):
                    if table[i+l-1-k][j] != table[i+k][j]:
                        flag = 0
                        break
                if flag:
                    if lmax <= l:
                        lmax = l
    print('#{} {}'.format(tc,lmax))