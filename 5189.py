import sys
sys.stdin = open("5189.txt")

def dfs(c,cnt):
    global myMin
    if cnt >= myMin:
        return
    # print(order[:c])
    if visited.count(1) == N and c == 0:
        if myMin>cnt:
            myMin=cnt
        return

    for i in range(0,N):
        # cnt += data[0][i]
        if not visited[i]:
            visited[i] = 1
            order[c] = i
            dfs(i,cnt+data[c][i])
            visited[i] = 0



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    order = [0]*N
    visited = [0]*N
    myMin = 987654321

    dfs(0,0)
    print("#{} {}".format(tc,myMin))