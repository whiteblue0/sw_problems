import sys
sys.stdin = open("4012.txt")

def taste(lst):
    t = 0
    for i in lst:
        for j in lst:
            t += data[i][j]
    return t


def comb(c,idx):
    global result
    if c == K:
        div2 = []
        for i in range(N):
            if i not in div1:
                div2.append(i)
        diff = abs(taste(div1) - taste(div2))
        if diff < result:
            result = diff
        return
    for i in range(idx,N):
        div1[c] = i
        comb(c+1,i+1)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    result = 0xffffff
    K = int(N/2)
    div1 = [0]*K

    comb(0,0)
    print("#%d" % tc,result)
