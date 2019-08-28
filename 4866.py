import sys
sys.stdin = open('괄호검사.txt')


T = int(input())
for tc in range(1,T+1):
    stack = []
    result = 1
    N = input()
    braket = 0
    cbrace = 0
    for i in N:
        if i == '(' or i == '{' or i == ')' or i == '}':
            stack.append(i)
    while stack:
        check = stack.pop()
        if check == ')':
            braket += 1
            if stack[-1] == '{':
                result = 0
                break
        elif check == '}':
            cbrace += 1
            if stack[-1] == '(':
                result = 0
                break
        elif check == '(':
            braket -= 1
        else:
            cbrace -= 1

        if not braket and not cbrace:
            result = 1
        else:
            result = 0


    print('#{} {}'.format(tc,result))

