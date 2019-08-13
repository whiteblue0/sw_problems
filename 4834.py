import sys
sys.stdin = open('4834.txt')

T = int(input())

for a in range(1,T+1):
    N = int(input())
    num = input()
    length = len(num)
    num = int(num)

    table = [0]*10

    for i in range(length):
        table[num % 10] +=1
        num //= 10

    mynum = 0
    cnt = 0
    for i in range(len(table)):
        if cnt <= table[i]:
            cnt = table[i]
            mynum = i
    print('#{} {} {}'.format(a, mynum, cnt))