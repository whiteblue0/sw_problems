import sys
sys.stdin = open('input.txt')

Case = int(input())

for i in range(1,Case+1):
    P,Q,R,S,W = map(int,input().split())

    A = P*W
    if W <= R:
       B = Q
    else:
       B = Q + S*(W-R)

    if A < B:
        print('#{} {}'.format(i,A))
    else:
        print('#{} {}'.format(i,B))