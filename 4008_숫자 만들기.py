def calc(value, i, op):
    if op == 0 :
        return value + nums[i]
    elif op == 1 :
        return value - nums[i]
    elif op == 2 :
        return value * nums[i]
    elif op == 3 :
        return int(value / nums[i])

    return 0

def dfs(k, rst):
    global myMax, myMin
    if k == N-1:
        myMax = max(rst, myMax)
        myMin = min(rst, myMin)
        return

    for i in range(4):
        if oper[i] == 0: continue
        oper[i] -= 1
        dfs(k + 1, calc(rst, k+1, i))
        oper[i] += 1

import sys
sys.stdin = open("4008.txt")
T = int(input())
for tc in range(1, T+1):
    myMax = -987654321
    myMin = 987654321
    N = int(input())    # 숫자개수
    oper= list(map(int, input().split()))  # 연산자
    nums = list(map(int, input().split())) # 숫자

    dfs(0, nums[0])
    result = myMax - myMin
    print("#{} {}".format(tc, result))


