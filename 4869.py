import sys
sys.stdin = open('종이붙이기.txt')

def tape(N,cnt):
    global result
    if N == 0:
        result += cnt
    if N >= 10:
        tape(N-10,cnt)
    if N >= 20:
        tape(N-20,cnt*2)

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    result = 0
    tape(N,1)
    print('#{} {}'.format(tc,result))
