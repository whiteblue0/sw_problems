import sys
sys.stdin = open('1209.txt')

T = 10

for a in range(1,T+1):
    N = int(input())

    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    Rdiago = 0
    Ldiago = 0
    for i in range(100):
        Rdiago += arr[i][i]
        Ldiago += arr[i][99-i]

    rowmax = 0
    colmax = 0
    for j in range(100):
        temp = 0
        temp2 = 0
        for i in range(100):
            temp += arr[i][j]
            temp2 += arr[j][i]
        if rowmax <= temp:
            rowmax = temp
        if colmax <= temp2:
            colmax = temp2

    arrmax = 0
    table = [Rdiago,Ldiago, rowmax, colmax]
    for i in table:
        if arrmax <= i:
            arrmax = i

    print('#{} {}'.format(a, arrmax))
