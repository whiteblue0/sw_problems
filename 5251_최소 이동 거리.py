import sys
sys.stdin = open("5251.txt")
import collections

def bfs(s):
    que = collections.deque()
    que.append(s)
    dist[s] = 0
    while que:
        t = que.popleft()
        for i in range(len(data[t])):
            temp = dist[t] + data[t][i][1]
            if dist[data[t][i][0]] > temp:
                dist[data[t][i][0]] = temp
                que.append(data[t][i][0])


T = int(input())
for tc in range(1,T+1):
    N,E = map(int, input().split())
    data = dict()
    for i in range(N+1):
        data[i] = []

    for i in range(E):
        temp = list(map(int, input().split()))
        data[temp[0]].append([temp[1],temp[2]])
    dist = [0x7ffffff]*(N+1)
    print(data)
    bfs(0)
    print("#{} {}".format(tc,dist[-1]))