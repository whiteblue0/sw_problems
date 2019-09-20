import sys
sys.stdin = open("5202.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x : x[1])
    cnt = 0
    end = 0
    for i in range(N):
        if end <= data[i][0]:
            cnt += 1
            end = data[i][1]
    print('#{} {}'.format(tc, cnt))