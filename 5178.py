import sys
sys.stdin = open("5178.txt")

def postorder(node):
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        if tree[node][0] != 0 or tree[node][1] !=0:
            tree[node][3] = tree[tree[node][0]][3] + tree[tree[node][1]][3]


T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
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

    for i in range(M):
        n, num = map(int,input().split())
        tree[n][3] = num

    # for _ in range(N+1):
    #     print(_,tree[_])
    postorder(1)

    print("#{} {}".format(tc,tree[L][3]))
