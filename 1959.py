import sys
sys.stdin = open("input.txt")

T = int(input())

for x in range(T):
    m, n = map(int, input().split())

    # lst1 = list(map(int, input().split()))      #m
    # lst2 = list(map(int, input().split()))      #n
    cnt = 0
    result = 0

    if m < n :
        row = m
        lst1=list(map(int,input().split()))  # m
        lst2=list(map(int,input().split()))  # n
    else:
        row = n
        lst2=list(map(int,input().split()))  # n
        lst1=list(map(int,input().split()))  # m

    for k in range(abs(m-n)+1):
        for i in range(row):
            cnt += lst1[i]*lst2[i+k]
        if result < cnt:
            result = cnt
        cnt = 0
    print('#{} {}'.format(x+1,result))