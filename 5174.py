import sys
sys.stdin = open("subtree.txt")

def preorder(node):
    global cnt
    if node:
        cnt+=1
        preorder(tree[node][0])
        preorder(tree[node][1])

T = int(input())
for tc in range(1,T+1):
    E,N = map(int,input().split())
    data = list(map(int, input().split()))
    V = max(data)

    tree = [[0]*3 for _ in range(V+1)]

    for i in range(E):
        n1 = data[i*2]
        n2 = data[i*2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1

    # for i in range(V+1):
    #     print(i,tree[i])
    cnt=0
    preorder(N)
    print("#{} {}".format(tc,cnt))
