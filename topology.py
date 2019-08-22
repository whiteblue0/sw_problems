import sys
sys.stdin = open('1267.txt')


V, E = map(int, input().split())
temp = list(map(int,input().split()))
data = []


for i in range(E):
    data.append((temp[i], temp[i+1]))



adj_list = [[] for i in range(V+1)]
indegree = [0 for i in range(V+1)]
queue = []
result = []


def addEdge(u, v):
    adj_list[u].append(v)
    indegree[v]+=1

def topologicalSort():
    for v in range(1, V+1):
        if indegree[v] == 0:
            queue.append(v)

    for i in range(V):
        if not queue:
            print("has Cycle")
            return False

        cur = queue.pop(0)
        result.append(cur)
        for adj in adj_list[cur]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                queue.append(adj)

    return True


for i in range