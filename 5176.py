import sys
sys.stdin = open("5176.txt")

def interorder(node):
    global num
    if node:
        interorder(tree[node][0])
        num += 1
        tree2[node] = num
        interorder(tree[node][1])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    tree2 = [[0]*3 for _ in range(N+1)]
    cnt = 1
    for i in range(1,N+1):
        tree[i][2] = i // 2
        if cnt == N:
            continue
        cnt += 1
        tree[i][0] = cnt
        if cnt == N:
            continue
        cnt += 1
        tree[i][1] = cnt

    num=0
    interorder(1)
    print("#{} {} {}".format(tc,tree2[1],tree2[N//2]))

