import sys
sys.stdin = open("1859.txt")

T = int(input())

for a in range(1,T+1):
    N = int(input())
    table = list(map(int, input().split()))


    cnt = 0
    top = max(table)
    startidx = 0
    endidx = table.index(max(table))

    while startidx < len(table):
        for i in range(startidx,endidx):
            cnt += top - table[i]

        startidx = endidx + 1
        temp = 0
        for i in range(startidx,len(table)):
            if temp <= table[i]:
                endidx = i

        # if table[startidx:]:
        #     endidx = table.index(max(table[startidx:]))

        top = table[endidx]
        print('리스트 길이:',len(table))
        print('{}번째 케이스 start:{} end{} cnt={}'.format(a,startidx, endidx,cnt))

    print('#{} {}'.format(a,cnt))

