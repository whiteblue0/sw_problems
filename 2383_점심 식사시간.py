import sys
sys.stdin = open("2383.txt")
from collections import deque

def goStair(lst,stair,K):
    global cnt
    que = deque()
    priority=[0]*len(lst)
    for i in range(len(lst)):
        # print('lst[i][0],stair[0],lst[i][1],stair[1]:',lst[i][0],stair[0],lst[i][1],stair[1])
        priority[i]=(abs(lst[i][0]-stair[0])+abs(lst[i][1]-stair[1]))
    priority.sort()
    print(priority)
    cnt = 0
    while priority:
        while que:
            if que[0] == 0:
                que.popleft()
            else:
                break
        for i in range(len(que)):
            que[i] -= 1
        cnt += 1
        if priority[0] != 0:
            for i in range(len(priority)):
                priority[i] -= 1
            while (len(que) < 3) and (len(que) > 0) :
                if len(priority) == 0:
                    break
                elif priority[0] == 0:
                    que.append(K)
                    priority.pop(0)
                else:
                    break
        else:
            if len(que) == 3:
                pass
            else:
                que.append(3)
                priority.pop(0)
    print(que,cnt)
    if que:
        cnt += max(que)

def comb(c, idx):
    global cnt, result
    print('stair1:',stair1[:c])
    goStair(stair1[:c],[stairs[0][0],stairs[0][1]],stairs[0][2])
    temp1 = cnt
    stair2 = []
    for n in range(M):
        if people[n] not in stair1[:c]:
            stair2.append(people[n])
    print('stair2:',stair2)
    goStair(stair2, [stairs[1][0], stairs[1][1]], stairs[1][2])
    temp2 = cnt
    print('temp1, temp2:',temp1, temp2)
    print()
    if temp1 < temp2:
        temp = temp2
    else:
        temp = temp1
    if temp < result:
        result = temp

    if c == M:
        return
    for i in range(idx,M):
            stair1[c] = people[i]
            comb(c+1,i+1)

T = int(input())
for tc in range(2):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    for _ in range(N):
        print(data[_])
    people = []
    stairs = []

    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                people.append([i,j])
            elif data[i][j] > 1 :
                stairs.append([i,j,data[i][j]])

    print(people)
    print(stairs)
    M = len(people)
    visited = [0]*M
    stair1 = [0]*M
    result = 0xfffffff
    comb(0,0)
    print('#{} {}'.format(tc+1, result))