import sys
sys.stdin = open("1242.txt")

def verify(lst):
    ans = (lst[0]+lst[2]+lst[4]+lst[6])*3 + (lst[1]+lst[3]+lst[5]) + lst[7]
    if ans % 10 == 0:
        return sum(lst)
    else:
        return 0

def decode(code):
    result = ''
    for i in range(8):
        num=''
        for j in range(7):
            num += code[i*7+j]



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

decoder = ['0001101',
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
    data = []
    for _ in range(N):
        tmp = input()
        if _ == 0:
            data.append(tmp)
        elif tmp == data[-1]:
            continue
        else:
            data.append(tmp)
    for _ in range(len(data)):
        print(data[_])
    print()
    result = 0
    for i in range(len(data)):
        m = M-1
        while m:
            k = 1
            if data[i][m] != '0' and m>=13:
                adder = ""
                for c in range(14):
                    adder += table[data[i][m - 13 + c]]
                print(adder)
                print(adder[-7*k:])
                if adder[-7*k:] in decoder:
                    for ck in range()

                m -= 14
            else:
                m -= 1

