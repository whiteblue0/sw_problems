import sys
sys.stdin = open("1248.txt")

def preorder(node):
    global vol
    if node != 0:
        # print("{}".format(node),end=" ")
        vol.append(node)
        preorder(tree[node][0])
        preorder(tree[node][1])

T = int(input())
for tc in range(1,T+1):
    V, E, s1, s2 = map(int,input().split())
    data = list(map(int,input().split()))

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

    vol = []
    lst1 = []
    lst2 = []
    stack = []
    stack.append(s1)
    while stack:
        v = stack.pop()
        nv = tree[v][2]
        if nv == 0:
            break
        lst1.append(nv)
        stack.append(nv)

    stack = []
    stack.append(s2)
    while stack:
        v = stack.pop()
        nv = tree[v][2]
        if nv == 0:
            break
        lst2.append(nv)
        stack.append(nv)

    for i in lst1:
        if i in lst2:
            ancestor = i
            break   
    preorder(ancestor)

    print("#{} {} {}".format(tc,ancestor,len(vol)))
