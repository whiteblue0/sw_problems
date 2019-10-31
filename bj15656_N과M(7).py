N,M = map(int, input().split())
data = list(map(int, input().split()))

def permu1(c):
    print(result[:M])
    if c == M:
        # print(result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result[c] = data[i]
            permu1(c+1)
            visited[i]=0


K = 5
data = [1,2,3,4,5,6]
visited = [0]*N
result = [0]*K

permu1(0)