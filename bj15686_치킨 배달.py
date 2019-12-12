from collections import deque
# 우, 하 , 좌, 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def getchickdist(lst):
    cnt = 0
    for i in range(len(lst)):
        y= chicklst[lst[i]][0]
        x= chicklst[lst[i]][1]
        data[y][x] = 0
    for i in range(len(house)):
        dist = 0xfffffff
        sy = house[i][0]
        sx = house[i][1]
        for j in range(len(chicklst)):
            if j not in lst:
                ey,ex = chicklst[j][0],chicklst[j][1]
                temp = abs(ey-sy) + abs(ex-sx)
                if dist > temp:
                    dist = temp
        cnt += dist

    for i in range(len(lst)):
        y= chicklst[lst[i]][0]
        x= chicklst[lst[i]][1]
        data[y][x] = 2
    return cnt



def comb(c,idx):
    global result
    if c == M:
        # print(close)
        gap = getchickdist(close)
        if result > gap:
            result = gap
        return

    for i in range(idx,len(chicklst)):
        # close[c] = i
        store[c] = i
        comb(c+1, i+1)



N,M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
result = 0xfffffff
chicklst = []
house = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            chicklst.append([i,j])
        elif data[i][j] == 1:
            house.append((i,j))

K = len(chicklst) - M
close = [0]*K
store = [0]*M
comb(0,0)

print(result)