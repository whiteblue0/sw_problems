
def getstatus(pipe):
    # 가로
    if pipe[1][0]-pipe[0][0] == 0:
        return 0
    # 세로
    elif pipe[1][1]-pipe[0][1] == 0:
        return 2
    # 대각선
    else:
        return 1

# pipe 좌표, pipe상태, 방향
def shift(p,s,i):
    c = [[0,0],[0,0]]
    for y in range(2):
        for x in range(2):
            c[y][x] = p[y][x]
    # 가로상태
    if s == 0:
        # 가로>>가로
        if i == 0:
            # tail
            c[0][1] += 1
            # head
            c[1][1] += 1
        # 가로>>대각선
        elif i == 1:
            # tail
            c[0][1] += 1
            # head
            c[1][0] += 1
            c[1][1] += 1
    # 대각선상태
    elif s == 1:
        # 대각선>>가로
        if i == 0:
            # tail
            c[0][0] += 1
            c[0][1] += 1
            # head
            c[1][1] += 1
        # 대각선>>대각선
        elif i == 1:
            # tail
            c[0][0] += 1
            c[0][1] += 1
            # head
            c[1][0] += 1
            c[1][1] += 1
        # 대각선>>세로
        else:
            # tail
            c[0][0]+=1
            c[0][1]+=1
            # head
            c[1][0] += 1
    # 세로상태
    else:
        # 세로>>대각선
        if i == 1:
            # tail
            c[0][0] += 1
            # head
            c[1][0] += 1
            c[1][1] += 1
        # 세로>>세로
        elif i == 2:
            # tail
            c[0][0] += 1
            # head
            c[1][0] += 1
    return c

def ispass(p,status):
    # mapcheck
    hy,hx = p[1][0],p[1][1]
    # print("hy,hx:",hy,hx)
    # print("status:",status)
    if not 0 <= hy < N or not 0 <= hx < N:
        # print("ispass p:", p)

        return False

    # wallcheck

    if status == 1:
        if data[hy][hx]+data[hy-1][hx]+data[hy][hx-1]:
            # print("wall",data[hy][hx], data[hy-1][hx], data[hy][hx-1])
            return False
    else:
        if data[hy][hx] == 1:
            # print("wall",data[hy][hx])
            return False

    # visitedcheck
    if visited[hy][hx]:
        return False
    return True


def dfs(p):
    global cnt
    # print(p)
    status = getstatus(p)
    head = p[1]
    # print(head)
    if head == [N-1,N-1]:
        cnt += 1

    for i in range(3):
        if abs(status-i) == 2:
            continue
        # print("i:",i)
        np = shift(p,status,i)

        if ispass(np,i):
            # print(p, ">>", np)
            dfs(np)


N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
pipe = [[0,0],[0,1]]
visited = [[0]*N for _ in range(N)]
cnt = 0

dfs(pipe)
print(cnt)