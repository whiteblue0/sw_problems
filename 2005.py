import sys
sys.stdin = open('2005.txt')


T = int(input())
build = [[1]]
lst = [1, 1]

for a in range(1,T+1):
    N = int(input())
    if N == 1:
        print('#{} \n1'.format(a))
    else:
        lst2 = [1]
        for i in range(1,N):
            lst2.append(lst[i]+lst[i-1])
        lst2.append(1)
        build.append(lst)

        lst = lst2
        print('#{}'.format(a))
        for y in range(len(build)):
            for x in range(len(build[y])):
                if x == len(build[y])-1:
                    print(build[y][x])
                else:
                    print(build[y][x],end=' ')