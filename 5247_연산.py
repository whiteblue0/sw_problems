import sys
sys.stdin = open("5247.txt")
import collections

def ispass(x):
    return 1<=x<=1000000


def bfs(s):
    global counter
    que = collections.deque()
    que.append(s)
    counter[s] = 0
    while que:
        t = que.popleft()
        if t== M:
            break
        for i in range(4):
           if ispass(D[i](t)) and not counter[D[i](t)]:
               que.append(D[i](t))
               counter[D[i](t)] = counter[t] + 1

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    counter = [0]*(1000000+1)
    D = [lambda x:x+1,lambda x:x-1,lambda x:x*2,lambda x:x-10]

    bfs(N)
    print("#{} {}".format(tc,counter[M]))