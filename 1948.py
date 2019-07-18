import sys
sys.stdin = open('input.txt')

T = int(input())

callendar = {
    1:31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
for j in range(1,T+1):
    m1, d1, m2, d2 = map(int,input().split())


    date = 1

    for i in range(m1,m2):
        date+=callendar[i]
    date -= d1
    date += d2


    print('#{} {}'.format(j,date))