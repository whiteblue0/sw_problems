import sys
sys.stdin = open('input.txt')

T = int(input())

for k in range(T):
    N = int(input())

    arr0 = []
    for i in range(N):
        arr0.append(list(map(int, input().split())))

    def rot(ary1,ary0):
        for y in range(N):
            for x in range(N):
                ary1[x][N-1-y]= ary0[y][x]
        return ary1

    arr1 = [[0] * N for i in range(N)]
    arr1 = rot(arr1,arr0)
    arr2 = [[0] * N for i in range(N)]
    arr2 = rot(arr2,arr1)
    arr3 = [[0] * N for i in range(N)]
    arr3 = rot(arr3,arr2)

    for j in range(N):
        for i in range(N):
            arr1[j][i] = str(arr1[j][i])
            arr2[j][i] = str(arr2[j][i])
            arr3[j][i] = str(arr3[j][i])

    for j in range(N):
        arr1[j]=''.join(arr1[j])
        arr2[j]=''.join(arr2[j])
        arr3[j]=''.join(arr3[j])
    print('#%d' % (k+1))
    for i in range(N):
        print('{} {} {}'.format(arr1[i],arr2[i],arr3[i]))