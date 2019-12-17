N,M = map(int, input().split())

def comb(c,idx):

    if c == M:
        print(' '.join(result[:M]))
        return

    for i in range(idx,N):
        if not visited[i]:
            result[c] = str(i+1)
            comb(c+1,i+1)

result = [0]*M
visited = [0]*N

comb(0,0)