import sys
sys.stdin = open('input.txt')

T = int(input())

def snail(size):
    cnt = 1

    Matrix = [[0]*size for i in range(size)]
    y= 0

    a = 1
    b = size
    d = -1


    for x in range(size):
        Matrix[y][x]=cnt
        cnt+=1

    while cnt < (size**2):
        for y in range(a,b):
            Matrix[y][x]=cnt
            cnt+=1

        for x in range(b-2,d,-1):
            Matrix[y][x]=cnt
            cnt+=1

        for y in range(b - 2, d + 1, -1):
            Matrix[y][x]=cnt
            cnt+=1

        for x in range(a , b -1):
            Matrix[y][x] = cnt
            cnt+=1

        a += 1
        b -= 1
        d += 1


    for j in range(size):
        for i in range(size):
            print(Matrix[j][i],end=' ')
        print('')


for i in range(1,T+1):
    size = int(input())
    print('#{}'.format(i))
    snail(size)