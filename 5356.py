import sys
sys.stdin = open('5356.txt')

T = int(input())
for tc in range(1,T+1):
    N = 5
    matrix = [[0]*15 for _ in range(N)]

    for i in range(N):
        temp = input()
        for j in range(len(temp)):
            matrix[i][j] = temp[j]

    print('#{}'.format(tc),end=' ')
    for i in range(15):
        for j in range(N):
            if matrix[j][i]:
                print(matrix[j][i],end='')
    print()
