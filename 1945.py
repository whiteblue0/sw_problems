import sys
sys.stdin = open('input.txt')

T = int(input())


a,b,c,d,e, = 0, 0, 0, 0, 0

# num = (2**a) * (3**b) * (5**b) * (7**d) * (11**e)

for i in range(1,T+1):
    num = int(input())
    while num>1:
        if num % 2 == 0:
            num /= 2
            a+=1

        if num % 3 == 0:
            num /= 3
            b += 1

        if num % 5 == 0:
            num /= 5
            c += 1

        if num % 7 == 0:
            num /= 7
            d += 1

        if num % 11 == 0:
            num /= 11
            e += 1


    print('#{}'.format(i),a,b,c,d,e)
    a, b, c, d, e, = 0, 0, 0, 0, 0
