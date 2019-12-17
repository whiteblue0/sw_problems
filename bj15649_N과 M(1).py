N,M = map(int, input().split())

def permu(c):

    if c == M:
        print(' '.join(result[:M]))
        return

    for i in range(N):
        if not visited[i]:
            result[c] = str(i+1)
            visited[i] = 1
            permu(c+1)
            visited[i] = 0

result = [0]*N
visited = [0]*N

permu(0)