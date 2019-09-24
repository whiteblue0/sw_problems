import sys
sys.stdin = open("5248_그룹나누기_input.txt")

def merge(a,b):
    flag = 0
    if a > b:
        a,b = b,a
    for i in range(1,M+1):
        for j in group[i]:
            if j == a or j == b:
                flag = 1
                point = i
                break

    if flag:
        group[point].add(a)
        group[point].add(b)
        P[a] = 1
        P[b] = 1
    else:
        group[a].add(a)
        group[a].add(b)
        P[a] = 1
        P[b] = 1


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    temp = list(map(int, input().split()))
    data = [0]*M
    for i in range(M):
        data[i] = [temp[i*2],temp[i*2+1]]
    group = [set() for _ in range(N+1)]
    P = [0]*(N+1)
    for i in range(M):
        merge(data[i][0],data[i][1])
        # print(data[i][0],data[i][1])
    for i in range(1,N+1):
        if not P[i]:
            group[i].add(i)
    # print(group)
    cnt = 0
    for i in range(N+1):
        if group[i]:
            cnt += 1
    # print(cnt)

    print("#{} {}".format(tc,cnt))
