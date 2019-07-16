import sys
sys.stdin = open('input.txt')

Totalcase = int(input())

for i in range(1,Totalcase+1):
    Testcase = input()
    palin = Testcase[::-1]
    if palin == Testcase :
        print('#{} {}'.format(i,1))
    else:
        print('#{} {}'.format(i,0))
