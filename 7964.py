import sys
sys.stdin = open('7964.txt')

def Leftlink(x):
    nextp = 0
    flag = 1
    for i in range(D,-1,-1):
        if lines[x-i]:
            nextp = x-i
            break
        else:
            flag = 0

    if nextp:
        return nextp
    else:
        return False



T = int(input())
for i in range()
    N,D = map(int, input().split())

    lines = list(map(int, input().split()))
    mark = []

    p = 0 #position
    cnt = 0

    for i in range(len(lines)):
        if i:
            position = i
            break
    print(lines)


# if lines[position]