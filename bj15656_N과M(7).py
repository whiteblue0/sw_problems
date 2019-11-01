N,M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()


def permu(c):
    if c == M:
        # print(result)
        for i in range(len(result)):
            if i == len(result) -1:
                print(result[i])
            else:
                print(result[i],end=' ')
        return

    for i in range(N):
        result[c] = data[i]
        permu(c + 1)


visited = [0]*N
result = [0]*M
ans = []

permu(0)


