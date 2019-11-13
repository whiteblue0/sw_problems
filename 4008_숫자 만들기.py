import sys
sys.stdin = open("4008.txt")


def dfs(oper,cnt):
    for i in range(N-1):
        if oper == 0 and opercnt[0]:
            opercnt[0] -= 1
            if opercnt[0] == 0:
                oper += 1
                oper %= 4
            cnt += numstack[i+1]
            dfs(oper ,cnt)
            opercnt[0] += 1

        elif oper == 1 and opercnt[1]:
            opercnt[1] -= 1
            if opercnt[1] == 0:
                oper += 1
                oper %= 4
            cnt -= numstack[i + 1]
            dfs(oper, cnt)
            opercnt[1] += 1
        elif oper == 2 and opercnt[2]:
            opercnt[2] -= 1
            if opercnt[2] == 0:
                oper += 1
                oper %= 4
            cnt *= numstack[i + 1]
            dfs(oper, cnt)
            opercnt[2] += 1
        elif oper == 3 and opercnt[3]:
            opercnt[3] -= 1
            if opercnt[3] == 0:
                oper += 1
                oper %= 4
            cnt /= numstack[i + 1]
            cnt = int(cnt)
            dfs(oper, cnt)
            opercnt[3] += 1


# input
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    opercnt = list(map(int,input().split()))
    numstack = list(map(int,input().split()))
    myMin = 0xfffffff
    myMax = 0
    for i in range(4):
        dfs(i,numstack[0])

    result = myMax - myMin
    print("#{} {}".format(tc,result))