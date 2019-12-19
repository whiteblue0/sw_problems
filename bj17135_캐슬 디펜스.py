def aim(p,enemy):
    # dp
    bowman = (N,p)
    dist = 0xfff
    for i in range(len(enemy)):
        if dist >= getDist(bowman,enemy[i]):
            dist = getDist(bowman,enemy[i])
    temp = []
    for i in range(len(enemy)):
        if dist == getDist(bowman,enemy[i]):
            temp.append(enemy[i])
    result = M
    for i in range(len(temp)-1,-1,-1):
        if temp[i][1] <= result:
            result = temp[i][1]
            target = temp[i]

    return target

def getDist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def play(bowmans,enemy):
    cnt = 0
    while enemy:
        # 조준
        target = []
        for position in bowmans:
            flag = 0
            for i in range(len(enemy)):
                if getDist([N,position],enemy[i]) <= D:
                    flag = 1
            if flag:
                temp = aim(position,enemy)
                if temp in target:
                    continue
                else:
                    target.append(temp)

        # 공격
        for i in range(len(target)):
            if target[i] in enemy:
                enemy.remove(target[i])
                cnt += 1
        # 적 이동
        if enemy:
            for i in range(len(enemy)-1,-1,-1):
                enemy[i][0] += 1
                # 성에 도착한 적 삭제
                if enemy[i][0] == N:
                    enemy.remove(enemy[i])
    return cnt

def comb(c,idx):
    global ans
    if c == 3:
        enemy = []
        for i in range(N, -1, -1):
            for j in range(M):
                if data[i][j]:
                    enemy.append([i, j])
        cnt = play(castle[:3],enemy)
        if ans < cnt:
            ans = cnt
        return

    for i in range(idx,M):
        castle[c] = i
        comb(c+1,i+1)



# 3 ≤ N, M ≤ 15     1 ≤ D ≤ 10
N,M,D = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(N)]
# 궁수의 위치
data.append([0]*M)
# 궁수의 개수 = 3
castle = [0]*M
ans = 0

comb(0,0)
print(ans)