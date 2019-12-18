from collections import deque

def getstatus(t,h):
    # idx: [0] == y, [1] == x

    # 가로
    if (h[0] - t[0]) == 0:
        return 0
    # 세로
    elif (h[1] - t[1]) == 0:
        return 2
    # 대각선
    else:
        return 1


def ispass(y,x,s):
    # ismap
    if y < 0 or y>= N or x < 0 or x >= N:
        return False

    # wallcheck
    if s == 1:
        if (data[y][x] + data[y-1][x] + data[y][x-1]) > 0:
            return False
    else:
        if data[y][x]:
            return False
    return True



def dfs(st,sh):
    global cnt
    que = deque()
    que.append((st,sh))

    while que:
        pipe = que.pop()
        tail,head = pipe[0], pipe[1]
        # print(pipe)
        # 파이프의 정렬상태 status: 0 == 가로, 1 == 대각선, 2 == 세로
        status=getstatus(tail,head)
        if head[0] == (N-1) and head[1] == (N-1):
            cnt+=1

        # 정렬상태 별 다음 좌표 초기화
        ntail=[head[0],head[1]]

        # 파이프가 대각선일 때
        if status == 1:
            for i in range(3):
                nhead=[0,0]
                if i==0:
                    # 대각선 진행
                    nhead[0],nhead[1]=head[0]+1,head[1]+1
                    if ispass(nhead[0],nhead[1],1):
                        que.append((ntail,nhead))
                elif i==1:
                    # 가로 진행
                    nhead[0],nhead[1]=head[0],head[1]+1
                    if ispass(nhead[0],nhead[1],0):
                        que.append((ntail,nhead))
                else:
                    # 세로 진행
                    nhead[0],nhead[1]=head[0]+1,head[1]
                    if ispass(nhead[0],nhead[1],2):
                        que.append((ntail,nhead))
        # 파이프가 가로일 때
        elif status == 0:
            for i in range(2):
                nhead=[0,0]
                if i == 0:
                    # 가로 진행
                    nhead[0], nhead[1] = head[0], head[1] + 1
                    if ispass(nhead[0],nhead[1],0):
                        que.append((ntail,nhead))
                else:
                    # 대각선 진행
                    nhead[0], nhead[1] = head[0] + 1, head[1] + 1
                    if ispass(nhead[0],nhead[1],1):
                        que.append((ntail,nhead))

        # 파이프가 세로일 때
        elif status == 2:
            for i in range(2):
                nhead=[0,0]
                if i == 0:
                    # 세로 진행
                    nhead[0], nhead[1] = head[0] + 1, head[1]
                    if ispass(nhead[0],nhead[1],2):
                        que.append((ntail,nhead))
                else:
                    # 대각선 진행
                    nhead[0], nhead[1] = head[0] + 1, head[1] + 1
                    if ispass(nhead[0],nhead[1],1):
                        que.append((ntail,nhead))


N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
# 도착점에 벽이 있어 못가는 경우
if data[N-1][N-1]:
    print(cnt)
# 그 외 경우
else:
    dfs([0,0],[0,1])
    print(cnt)
