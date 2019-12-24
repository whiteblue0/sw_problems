# 우, 하, 좌, 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def tilt(cmd):
    global flag,Rball,Bball
    checkR = [Rball[0], Rball[1]]
    checkB = [Bball[0], Bball[1]]
    # print(cmd)
    Rflag = 0
    Bflag = 0
    while True:
        if checkB == hole:
            flag = 0
            break
        else:
            Bball[0] = checkB[0]
            Bball[1] = checkB[1]
            if Rflag:
                Bball[0] -= dy[cmd]
                Bball[1] -= dx[cmd]


        if data[checkB[0]][checkB[1]] != 9:
            checkB[0]+=dy[cmd]
            checkB[1]+=dx[cmd]
        if [checkB[0],checkB[1]] == Rball:
            Rflag = 1

    while True:
        if not Bflag and checkR == hole:
            flag = 1
            break
        else:
            Rball[0] = checkR[0]
            Rball[1] = checkR[1]
            if Bflag:
                Rball[0] -= dy[cmd]
                Rball[1] -= dx[cmd]

        if data[checkR[0]][checkR[1]] != 9:
            checkR[0]+=dy[cmd]
            checkR[1]+=dx[cmd]
        if [checkR[0],checkR[1]] == Bball:
            Bflag = 1


def dfs(c):
    global ans,flag
    print(cmd,flag)
    # print(Rball,Bball)
    if not flag:
        return
    elif flag == 1:
        ans = c
        return

    if c == 11:
        ans = -1
        return

    for i in range(4):
        if not visited[c]:
            visited[c] = 1
            cmd[c] = i
            # print(c)
            tilt(i)
            # print()
            dfs(c+1)

            tilt((cmd[c]+2)%4)
            visited[c] = 0
            cmd[c] = 9



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