import sys
sys.stdin = open('4828.txt')

def mymax(lst):
    result = 0
    for i in range(len(lst)):
        if result <= lst[i]:
            result = lst[i]
    return result

def mymin(lst):
    result = lst[0]
    for i in range(len(lst)):
        if result >= lst[i]:
            result = lst[i]
    return result

T = int(input())

for a in range(1,T+1):
    N = int(input())
    tc = list(map(int, input().split()))
    result = mymax(tc) - mymin(tc)

    print('#{} {}'.format(a, result))