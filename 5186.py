import sys
sys.stdin = open('5186.txt')

T = int(input())
for tc in range(1,T+1):
    num = float(input())

    n = 1
    operand = num
    ans = ''
    while n != 13:
        if operand == 0:
            break
        k = round(2**(-n),n)
        if operand >= k:
            operand -= k
            ans += '1'
        else:
            ans +='0'

        n += 1
    if operand != 0:
        ans = 'overflow'

    print("#{} {}".format(tc,ans))