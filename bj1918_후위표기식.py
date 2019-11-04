isp = ['(', '+', '*']
icp = [0, '+', '*', '(']

data = input()

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
        fixlst.append(data[i])

while len(stack):
    fixlst.append(stack.pop())

print(''.join(list(map(str,fixlst))))