import sys
sys.stdin = open('input.txt')

def ispass(y,x):
    return 0<=y<N and 0<=x<N and not arr[y][x]

dy = [0,1,0,-1]
dx = [1,0,-1,0]


T = int(input())
N, K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

print(arr)
fit = 0
cnt = 0

y,x,d = 0,0,0

for i in range(N**2):
    if arr[y][x] == 1:
        cnt += 1
        ny, nx = y + dy[d], x + dx[d]
        if cnt == K :
            print('{} 들어갈 자리 하나'.format(K))
            if not ispass(ny, nx):
                print('다음줄')
                ny, nx = y + 1, 0
                fit += 1
                y, x = ny, nx
            if ispass(y,x) and arr[y][x+1] == 0:
                print('영역내')
                fit += 1

    elif arr[y][x] == 0:
        cnt = 0
        ny, nx = y + dy[d], x + dx[d]
        if not ispass(ny, nx):
            print('다음줄')
            ny, nx = y + 1, 0
        y, x = ny, nx


print(fit)