import sys
sys.stdin = open('반복문자 연습.txt')

T = int(input())

for tc in range(1,T+1):
    Word = input()

    stack = []
    stack.append(Word[0])
    for i in range(1,len(Word)):
        if not stack:
            stack.append(Word[i])
            continue
        elif stack[-1] == Word[i]:
            stack.pop()
            continue
        stack.append(Word[i])

    result = len(stack)

    print('#{} {}'.format(tc,result))