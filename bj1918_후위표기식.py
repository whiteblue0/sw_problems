priority = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}

data = input()

stack = []

for i in '('+data+')':
    if 'A' <= i <= 'Z':
        print(i,end='')
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while True:
            temp = stack.pop()
            if temp == '(':
                break
            print(temp,end='')
    else:
        while stack[-1] != '(' and priority[i] <= priority[stack[-1]]:
            print(stack.pop(), end='')
        stack.append(i)