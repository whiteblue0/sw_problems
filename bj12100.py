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
    # 0이 아닌 숫자들만 받아 인접한 숫자와 같은 숫자인지 확인
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            lst[i] *= 2
            lst[i+1] = 0

    # filteredLst에 0이 아닌 값만 저장
    filteredLst = []
    for i in range(len(lst)):
        if lst[i]:
            filteredLst.append(lst[i])
    # filteredLst의 길이가 N이 될 때까지 0 추가
    while len(filteredLst) < N:
        filteredLst.append(0)
    return filteredLst

def moveR(data):
    # 0번째부터 N번째 줄까지
    for i in range(N):
        que = []
        # 오른쪽부터 값을 받아 join함수로 숫자를 합칠수 있는지 확인
        for j in range(N-1,-1,-1):
            if data[i][j]:
                que.append(data[i][j])
        # print("before joined:",que)
        # 움직인 방향으로 합친 숫자 반환
        que = join(que)
        # print("after joined:",que)
        # que에 저장된 수행 결과를 데이터에 변환
        for j in range(N-1,-1,-1):
            data[i][j] = que[N-1-j]
    return data

def moveL(data):
    for i in range(N):
        que = []
        for j in range(N):
            if data[i][j]:
                que.append(data[i][j])
        que = join(que)
        for j in range(N):
            data[i][j] = que[j]
    return data

def moveD(data):
    for i in range(N):
        que = []
        for j in range(N-1,-1,-1):
            if data[j][i]:
                que.append(data[i][j])
        que = join(que)
        for j in range(N-1,-1,-1):
            data[j][i]=que[N-1-j]
    return data

def moveU(data):
    for i in range(N):
        que = []
        for j in range(N):
            if data[j][i]:
                que.append(data[i][j])
        que = join(que)
        for j in range(N):
            data[j][i] = que[j]
    return data


def move(data,d):
    controller={0: moveR,1: moveD,2: moveL,3: moveU}
    return controller[d](data)


def dfs(board,d,cnt):
    global ans
    board = move(board,d)

    if cnt == 5:
        mymax = checkmax(board)
        if ans < mymax:
            ans = mymax
        return
    for i in range(4):
            print(i)
            dfs(board,i,cnt+1)


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


# 4
# 2 2 2 2
# 2 2 2 2
# 2 2 2 2
# 2 2 2 2