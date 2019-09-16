import sys
sys.stdin = open("1240.txt")

def verify(lst):
    ans = (lst[0]+lst[2]+lst[4]+lst[6])*3 + (lst[1]+lst[3]+lst[5]) + lst[7]
    if ans % 10 == 0:
        return sum(lst)
    else:
        return 0
def iscode(ratio):
    for _ in range(4):
        if ratio[_] == 1:
            break
        else:
            for _2 in range(4):
                ratio[_2] //= 2
    
                



table = {'0':'0000',
         '1':'0001',
         '2':'0010',
         '3':'0011',
         '4':'0100',
         '5':'0101',
         '6':'0110',
         '7':'0111',
         '8':'1000',
         '9':'1001',
         'A':'1010',
         'B':'1011',
         'C':'1100',
         'D':'1101',
         'E':'1110',
         'F':"1111"}

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = [list(map(int,input())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M-1,-1,-1):
            if data[i][j]:
                for c in range(17):
                    if j-(14*c)+1 >0 and data[i][j-(14*c)+1]: