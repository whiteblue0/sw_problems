import sys
sys.stdin = open("1231.txt")

def interorder(node):
    if node != 0:
        interorder(tree[node][2])
        print("{}".format(tree[node][1]), end="")
        interorder(tree[node][3])
T = 10

for tc in range(1,T+1):
    V = int(input())
    tree = [[0]*4 for _ in range(V+1)]

    for i in range(1,V+1):
        nlst = [0,0,0,0]
        temp = input().split()
        for _ in range(len(temp)):
            if _ != 1:
                nlst[_] = int(temp[_])
            else:
                nlst[_] = temp[_]
        tree[i] = nlst
    print("#{}".format(tc),end=' ')
    interorder(1)
    print()