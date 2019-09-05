import sys,time
sys.stdin = open('1865.txt')

def dfs(x,cnt):
    global mymax
    if cnt<= mymax:
        return
    if x == N:
        if mymax<cnt:
            mymax=cnt
        return

    for y in range(N):
        if not visitied[y]:
            visitied[y] = 1

            dfs(x+1,cnt*0.01*person[y][x])

            visitied[y] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    visitied = [0]*N
    person = []
    for _ in range(N):
        person.append(list(map(int,input().split())))
    mymax = 0

    dfs(0,1)
    mymax = mymax*100
    result = round(mymax,6)

    print('#{} {:6f}'.format(tc,result))

