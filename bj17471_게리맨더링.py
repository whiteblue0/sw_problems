def islinked(lst):
    if len(lst) == 0:
        return False
    stack = []
    visited = [0]*N
    s = lst[0]
    visited[0] = 1
    stack.append(s)
    while stack:
        c = stack.pop()
        for i in range(N):
            if waypointer[c][i] and not visited[i]:
                visited[i] = 1
                stack.append(i)
    for i in lst:
        if not visited[i]:
            return False
    return True

def vol(lst):
    temp = 0
    for i in lst:
        temp += people[i]
    return temp

def subset(c,idx):
    global result
    print(divison[:c])
    sector1 = divison[:c]
    sector2 = []
    for n in range(N):
        if n not in sector1:
            sector2.append(n)

    if islinked(sector1) and islinked(sector2):
        cnt = abs(vol(sector1) - vol(sector2))
        if cnt < result:
            result = cnt
        else:
            return

    if c == N:
        return

    for i in range(idx,N):
        divison[c] = i
        subset(c+1,i+1)

N = int(input())
people = list(map(int,input().split()))
linkspec = [list(map(int,input().split())) for _ in range(N)]
waypointer = [[0]*N for _ in range(N)]
divison = [0]*N
result = 0xfffffff

for i in range(N):
    for j in range(1,linkspec[i][0]+1):
        waypointer[i][linkspec[i][j]-1] = 1
        waypointer[linkspec[i][j]-1][i] = 1
# for i in range(N):
#     print(waypointer[i])

subset(0,0)
if result == 0xfffffff:
    result = -1
# print(result)