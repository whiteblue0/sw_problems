import sys
sys.stdin = open('4835.txt')

def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

T = int(input())
for x in range(1,T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    table = []
    for i in range(N-M+1):
        temp = 0
        for j in range(M):
                temp += lst[j+i]
        table.append(temp)

    BubbleSort(table)

    cnt = table[-1] - table[0]
    print('#{} {}'.format(x,cnt))