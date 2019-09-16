import sys
sys.stdin = open("1232.txt")

def postorder(node):
    global stack
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        stack.append(tree[node][3])



T = 10
for tc in range(1,T+1):
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

    # for _ in range(N+1):
    #     print(tree[_])
    # print()

    oper = ['+', '-', '*', '/']
    for i in range(N):
        temp = input().split()
        for j in range(len(temp)):
            if temp[j] in oper:
                continue
            else:
                temp[j] = int(temp[j])
        tree[temp[0]][3] = temp[1]

    # for _ in range(N+1):
    #     print(_,tree[_])

    stack = []
    postorder(1)
    cal = []
    while stack:
        operend = stack.pop(0)
        if operend == '+':
            n1 = cal.pop()
            n2 = cal.pop()
            result = n2 + n1
            cal.append(result)
        elif operend == '-':
            n1 = cal.pop()
            n2 = cal.pop()
            result = n2 - n1
            cal.append(result)
        elif operend == '*':
            n1 = cal.pop()
            n2 = cal.pop()
            result = n2 * n1
            cal.append(result)
        elif operend == '/':
            n1 = cal.pop()
            n2 = cal.pop()
            result = n2 // n1
            cal.append(result)
        else:
            cal.append(operend)
    print("#{} {}".format(tc,cal))