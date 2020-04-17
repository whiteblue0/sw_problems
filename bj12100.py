# 우, 하, 좌, 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def checkmax(data):
    mymax = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] > mymax:
                mymax = data[i][j]
    return mymax

def join(lst):
    i = 0
    while i < (len(lst)-1):
        if lst[i] == lst[i+1]:
            lst[i] = lst[i]*2
            lst[i+1] = 0
        i += 1
    for num in lst:
        if num == 0:
            lst.remove(0)

    for i in range(N-len(lst)):
        lst.append(0)
    return lst

def moveR(data):
    for i in range(N):
        que = []
        for j in range(N-1,-1,-1):
            if data[i][j]:
                que.append(data[i][j])
        print(que)
        que = join(que)
        print(que)
        for j in range(N-1,-1,-1):
            data[i][j] = que[N-1-j]



def moveD(data):
    pass

def moveL(data):
    pass

def moveU(data):
    pass

controller = {0:moveR, 1:moveD, 2:moveL, 3:moveU}
def move(data,d):
    # if d == 0:
    #     return moveR(data)
    # elif d == 1:
    #     return moveD(data)
    # elif d == 2:
    #     return moveL(data)
    # else:
    #     return moveU(data)
    return controller[d]()


def dfs(board,d,cnt):
    global ans
    board = move(board,d)

    if cnt == 5:
        mymax = checkmax(board)
        if ans < mymax:
            ans = mymax
            return
    for i in range(4):
        if i != d and not visited[cnt]:
            visited[cnt] = 1
            dfs(board,i,cnt+1)
            visited[cnt] = 0


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [0]*6

for i in range(4):
    dfs(data,i,1)

print(ans)


# 5
# 2 0 4 4 4
# 2 2 2 2 2
# 8 4 0 4 2
# 4 0 4 0 8
# 2 0 0 2 0
