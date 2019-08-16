import sys
sys.stdin = open('4839.txt')

T = int(input())

for a in range(1,T+1):
    P, A, B = map(int, input().split())

    l1 = 1
    l2 = 1
    r1 = P
    r2 = P
    result = 0
    while l1 <= r1 and l2 <= r2:
        c1 = (l1 + r1) // 2
        c2 = (l2 + r2) // 2
        if c1 == A:
            if c2 == B:
                result = 0
                break
            else:
                result = 'A'
                break
        elif c2 == B:
            result = 'B'
            break
        if c1 > A:
            r1 = c1
        else:
            l1 = c1
        if c2 > B:
            r2 = c2
        else:
            l2 = c2

    print('#{} {}'.format(a, result))