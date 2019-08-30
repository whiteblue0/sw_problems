import sys
sys.stdin = open('1224.txt')

isp = ['(', '+', '*']
icp = [0, '+', '*', '(']

T = 10

for tc in range(1,T+1):
    N = int(input())
    data = input()
    N = len(data)

    fixlst = []
    stack = []
    cnt = 0

    for i in range(len(data)):
        # print('i:',i,'data[i]:',data[i])
        # print('stack:',stack)
        # print('fixlst: ',fixlst)
        if data[i] == ')':
          while stack[-1] != '(':
              fixlst.append(stack.pop())
              if stack[-1] == '(':
                  stack.pop()
                  break

        elif data[i] in isp :
            if stack:
                if icp.index(data[i]) > isp.index(stack[-1]):
                    stack.append(data[i])
                else:
                    while stack and icp.index(data[i]) <= isp.index(stack[-1]):
                        fixlst.append(stack.pop())
                    stack.append(data[i])
            else:
                stack.append(data[i])
        else:
            fixlst.append(int(data[i]))

    while len(stack):
        fixlst.append(stack.pop())

    # print(fixlst,stack)

    result = 0
    for i in range(len(fixlst)):
        if fixlst[i] == '+':
            result =stack.pop()+stack.pop()
            stack.append(result)
        elif fixlst[i] == '*':
            result = stack.pop() * stack.pop()
            stack.append(result)
        else:
            stack.append(fixlst[i])

    print('#{} {}'.format(tc,result))
    
