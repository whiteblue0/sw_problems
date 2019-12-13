
def comb(c,idx):
    global result
    visited = [0] * N
    cnt = 0

    for j in reserve[:c]:
        # print(data[j][0])
        for d in range(data[j][0]):
            if j+d>=N:
                return
            visited[j+d] += 1

        for k in range(N):
            if visited[k] > 1:
                return

        cnt += data[j][1]
        if cnt > result:
            result = cnt

    if c == N:
        return

    for i in range(idx,N):
        reserve[c] = i
        comb(c+1,i+1)



N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

visited = [0]*N
reserve = [0]*N

result = 0
comb(0,0)
print(result)