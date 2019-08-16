import sys
sys.stdin = open('1259.txt')

T = int(input())

for a in range(T):
    N = int(input())
    screw = list(map(int, input().split()))
    lst = []
    cnt = []
    for i in range(N):
        lst.append([screw[2*i],screw[2*i+1]])

    for i in range(N):
        for j in range(N):
            if lst[i][0] == lst[j][1]:
                break
            if j == N-1:
                cnt.append(lst[i])
    while len(cnt) < len(lst):
        for i in range(N):
            if cnt[-1][1] == lst[i][0]:
               cnt.append(lst[i])
    print('#{} '.format(a+1), end='')
    for i in range(len(cnt)):
        print('{} {} '.format(cnt[i][0],cnt[i][1]),end='')
    print()
