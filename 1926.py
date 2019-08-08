import sys
sys.stdin = open('1926.txt')

T = int(input())

for i in range(1,T+1):
    w = str(i)
    cnt = 0
    for x in w:
        if x == '3' or x== '6' or x == '9':
            cnt+=1
    if cnt != 0:
        w = '-'*cnt

    if i == T:
        print(w)
    else:
        print(w, end= ' ')

