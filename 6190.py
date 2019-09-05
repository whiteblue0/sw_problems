import sys
sys.stdin = open('6190.txt')

# def check(num):
#     for i in range(len(num)):


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    base = list(map(int, input().split()))

    mono = 0
    for i in range(N-1):
        for j in range(i+1,N):
            num = str(base[i]*base[j])
            flag = 1
            for k in range(len(num) - 1):
                if num[k] > num[k + 1]:
                    flag = 0
                    break
            if flag :
                if mono < (int(num)):
                    mono = int(num)


    if mono:
        result = mono
    else:
        result = -1

    print('#{} {}'.format(tc,result))