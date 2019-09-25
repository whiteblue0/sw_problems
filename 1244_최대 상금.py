import sys
sys.stdin = open("1244.txt")

def Swap(prize, i, j):
    numArr = [0] * cardnum
    for k in range(cardnum-1, -1, -1):
        numArr[k] = prize % 10
        prize //= 10
    numArr[i], numArr[j] = numArr[j], numArr[i]
    prize = 0
    for k in range(cardnum):
        prize = prize * 10 + numArr[k]

    return prize

def findMax(prize, num, k):
    global ans
    for i in range(MAXSIZE):
        if mem[k][i] == 0:
            mem[k][i] = prize
            break
        elif mem[k][i] == prize:
            return

    if k == num:
        if prize > ans:
            ans = prize
    else:
        for i in range(cardnum-1):
            for j in range(i+1, cardnum):
                findMax(Swap(prize, i, j), num, k+1)

T = int(input())
MAXSIZE = 720
N = 10
for tc in range(1,T+1):
    mem = [[0] * MAXSIZE for _ in range(N+1)]
    prize, num = map(int, input().split())
    cardnum = 0
    ans = 0
    t = prize
    while(t):
        t //=10
        cardnum += 1
    findMax(prize, num, 0)

    print("#{} {}".format(tc, ans))