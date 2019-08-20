import sys
sys.stdin = open("1859.txt")

T = int(input())

for a in range(1,T+1):
    N = int(input())
    table = list(map(int, input().split()))


    cnt = 0
    top = max(table)
    startidx = 0
    maxidx = table.index(top)

    while startidx<len(table)-1:
        for i in range(startidx,maxidx):
            cnt+=top-table[i]

        top=0
        startidx=maxidx+1
        for i in range(startidx,len(table)):
            if table[i]>top:
                top=table[i]
                maxidx = i





    print('#{} {}'.format(a,cnt))

