import sys
sys.stdin = open("5177.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
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

    # for _ in range(N+1):
    #     print(_,tree[_])

    for i in range(1,N+1):
        tree[i][3] = data[i - 1]
        k = i
        while k:
            if tree[k][3] <= tree[tree[k][2]][3]:
                tree[k][3], tree[tree[k][2]][3] = tree[tree[k][2]][3], tree[k][3]
            k = tree[k][2]


    stack = []
    cnt = 0
    s = tree[N][2]
    stack.append(s)
    while stack:
        v = stack.pop()
        cnt += tree[v][3]
        if tree[v][2] !=0:
            stack.append(tree[v][2])
    print("#{} {}".format(tc,cnt))