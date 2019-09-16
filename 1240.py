import sys
sys.stdin = open("1240.txt")

def check(lst):
    ans = (lst[0]+lst[2]+lst[4]+lst[6])*3 + (lst[1]+lst[3]+lst[5]) + lst[7]
    if ans % 10 == 0:
        return sum(lst)
    else:
        return 0

table = ['0001101',
         '0011001',
         '0010011',
         '0111101',
         '0100011',
         '0110001',
         '0101111',
         '0111011',
         '0110111',
         '0001011']

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = [list(map(int,input())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M-1,-1,-1):
            if data[i][j] and j>=55:
                # print("i,j",i,j)
                k = j-55
                code = []
                for y in range(8):
                    temp = ['0','0','0','0','0','0','0']
                    for x in range(7):
                        if data[i][k+(7*y)+x]:
                            # print("[i][k+(7*y)+x]",i,k+(7*y)+x)
                            temp[x] = str(data[i][k+(7*y)+x])
                    temp = ''.join(temp)
                    if temp in table:
                        code.append(table.index(temp))
                    if len(code) == 8:
                        cnt = check(code)
                        if cnt:
                            result = cnt
                            break
                        else:
                            continue
    print("#{} {}".format(tc,result))
