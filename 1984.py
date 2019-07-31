import sys
sys.stdin = open('1984.txt')

T = int(input())

for i in range(T):
    N = list(map(int, input().split()))

    N.remove(max(N))
    N.remove(min(N))
    avg = round(sum(N)/len(N))
    print('#{} {}'.format(i+1, avg))
