# 우, 하, 좌, 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def tilt(cmd):
    global flag, Rball, Bball
    if cmd == 9:
        return
    checkR = [Rball[0], Rball[1]]
    checkB = [Bball[0], Bball[1]]
    # print(cmd)
    Rflag = 0
    Bflag = 0
    while data[checkB[0]][checkB[1]] != 9:

        if checkB == Rball:
            Rflag = 1
        if checkB == hole:
            flag = 0
            break

        checkB[0] += dy[cmd]
        checkB[1] += dx[cmd]

    checkB[0] -= dy[cmd]
    checkB[1] -= dx[cmd]
    if Rflag:
        checkB[0] -= dy[cmd]
        checkB[1] -= dx[cmd]

    while data[checkR[0]][checkR[1]] != 9:
        if checkR == Bball:
            Bflag = 1
        if checkR == hole:
            if not Bflag:
                flag = 1
            else:
                flag = 0
            break

        checkR[0] += dy[cmd]
        checkR[1] += dx[cmd]

    checkR[0] -= dy[cmd]
    checkR[1] -= dx[cmd]
    if Bflag:
        checkR[0] -= dy[cmd]
        checkR[1] -= dx[cmd]

    Rball = checkR
    Bball = checkB
    # print("Rball,Bball:",Rball,Bball)


def dfs(c):
    global ans,flag

    if not flag:
        ans = -1
        return

    # print("cmd,flag:",cmd[:c],flag)
    # print("c,flag:",c,flag)
    # print(Rball,Bball)
    cnt = 0
    for j in range(c-1):
        if cmd[j] == cmd[j+1]:
            continue
        tilt(cmd[j])
        cnt += 1
    if cnt > ans:
        ans = cnt

    if flag == 1:
        # ans = cnt
        # print("ans:",ans)
        return
    elif c == 11:
        return

    for i in range(4):
        if not visited[c]:
            visited[c] = 1
            cmd[c] = i
            dfs(c+1)
            visited[c] = 0




N,M = map(int,input().split())
data = [[0]*M for _ in range(N)]
visited = [0]*11
cmd = [9]*11
Rball = [] # 1
Bball = [] # 2
hole = []
flag = 2
ans = 0
for i in range(N):
    t = input()
    for j in range(len(t)):
        if t[j] == "#":
            data[i][j] = 9
        elif t[j] == ".":
            data[i][j] = 0
        elif t[j] == "B":
            data[i][j] = 2
            Bball = [i,j]
        elif t[j] == "R":
            data[i][j] = 1
            Rball = [i,j]
        else:
            data[i][j] = 3
            hole  = [i,j]

print("Rball,Bball:",Rball,Bball)
for i in range(N):
    print(data[i])
dfs(0)
print(ans)