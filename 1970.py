import sys
sys.stdin = open('input.txt')

T= int(input())

for i in range(T):
    N = int(input())


    x0 = N // 50000
    y0 = N % 50000

    x1 = y0 // 10000
    y1 = y0 % 10000

    x2 = y1 // 5000
    y2 = y1 % 5000

    x3 = y2 // 1000
    y3 = y2 % 1000

    x4 = y3 // 500
    y4 = y3 % 500

    x5 = y4 // 100
    y5 = y4 % 100

    x6 = y5 // 50
    y6 = y5 % 50

    x7 = y6 // 10
    y7 = y6 % 10

    print('#{}'.format(i+1))
    print('{} {} {} {} {} {} {} {}'.format(x0,x1,x2,x3,x4,x5,x6,x7))
