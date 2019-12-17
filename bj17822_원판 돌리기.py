from collections import deque

def rotate(lst,dir,k):
    if dir:
        for i in range(k):
            lst.append(lst.popleft())
    else:
        for i in range(k):
            lst.appendleft(lst.pop())
    return lst


N,M,T = map(int, input().split())
board = [deque() for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in temp:
        board[i].append(j)

# cmd[i] = [x,d,k]
cmd = [list(map(int, input().split())) for _ in range(T)]
cnt = 0
while cnt < T:
    X = cmd[cnt][0]
    D = cmd[cnt][1]
    K = cmd[cnt][2]
    for i in range(N):
        if (i+1) % X == 0:
            temp = rotate(board[i],D,K)
            board[i] = temp

    checker = [[0]*M for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                if i < N-1 and board[i][j] == board[i+1][j]:
                    checker[i][j] = 1
                    checker[i+1][j] = 1
                    flag = 1
                if board[i][j] == board[i][j-1]:
                    checker[i][j] = 1
                    checker[i][j-1] = 1
                    flag = 1

    for i in range(N):
        for j in range(M):
            if checker[i][j]:
                board[i][j] = 0

    if not flag:
        avg = 0
        mysum = 0
        mylen = 0
        for i in range(N):
            for j in range(M):
                if board[i][j]:
                    mylen += 1
                    mysum += board[i][j]
        if mylen:
            avg = mysum / mylen

            for i in range(N):
                for j in range(M):
                    if board[i][j] == 0:
                        continue
                    elif board[i][j] > avg:
                        board[i][j] -= 1
                    elif board[i][j] < avg:
                        board[i][j] += 1

    cnt += 1

ans = 0
for i in range(N):
    for j in range(M):
        ans += board[i][j]

print(ans)