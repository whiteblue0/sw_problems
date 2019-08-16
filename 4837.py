import sys
sys.stdin = open("4837.txt")

T = int(input())

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for a in range(1,T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1, 1<<len(arr)):
        sum = 0
        temp = []
        for j in range(len(arr)):
            if i & (1<<j):
                sum += arr[j]
                temp.append(arr[j])
        if sum == K and len(temp) == N:
            cnt +=1
    print('#{} {}'.format(a, cnt))