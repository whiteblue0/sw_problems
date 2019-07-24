import sys
sys.stdin = open('input.txt')

T = int(input())
for k in range(T):
    N = int(input())
    tcase = list(map(int, input().split()))
    tcase.sort()
    print('#{}'.format(k+1),end=' ')
    for i in range(len(tcase)):
        if i == len(tcase) - 1:
            print(tcase[i])
        else:
            print(tcase[i],end=' ')