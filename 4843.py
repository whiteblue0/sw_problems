import sys
sys.stdin = open("4843.txt")

T = int(input())

for a in range(1,T+1):
    N = int(input())
    table = list(map(int, input().split()))
    result = []

    while table:
        if len(result) == 10:
            break
        tmax = table[0]
        maxidx = 0
        tmin = table[0]
        minidx = 0
        for i in range(len(table)):
            if tmax <= table[i]:
                tmax = table[i]
                maxidx = i
            if tmin >= table[i]:
                tmin = table[i]
                minidx = i

        result.append(tmax)
        result.append(tmin)

        table.remove(tmax)
        table.remove(tmin)

    print('#{}'.format(a),end=' ')
    for i in result:
        print(i,end=' ')
    print()