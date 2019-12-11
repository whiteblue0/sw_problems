def calc(value, i, op):
    if op == 0:
        return value + nums[i]
    elif op == 1:
        return value - nums[i]
    elif op == 2:
        return value * nums[i]
    elif op == 3:
        return int(value / nums[i])

    return 0

def dfs(c, cnt):
    global mymax, mymin
    if c == N-1:
        mymax = max(cnt, mymax)
        mymin = min(cnt, mymin)
        return

    for i in range(4):
        if operdata[i] == 0:
            continue
            operdata[i] -= 1
        dfs(c + 1, calc(cnt, c+1, i))
        operdata[i] += 1


mymax = -0xfffffff
mymin = 0xfffffff
N = int(input())    # 숫자개수
nums = list(map(int, input().split())) # 숫자
operdata= list(map(int, input().split()))  # 연산자

dfs(0, nums[0])

print(mymax)
print(mymin)