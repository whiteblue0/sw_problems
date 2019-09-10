import sys
sys.stdin = open("1232.txt")

T = 10
N = int(input())

tree = [[0]*4 for _ in range(N+1)]
temp = 1
for i in range(1,N+1):
    tree[i][2] = i // 2
    if temp == N:
        continue
    temp += 1
    tree[i][0] = temp
    if temp == N:
        continue
    temp += 1
    tree[i][1] = temp

oper = ['+', '-', '*', '/']
for i in range(N):
    temp = input().split()
    for j in temp:
        if j in oper:
            continue
        else:
            j = int(j)
    print(temp)
    tree[temp[0]][3] = temp[1]

for _ in range(N+1):
    print(tree[_])