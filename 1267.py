import sys
sys.stdin = open('1267.txt')

<<<<<<< HEAD
def find():
    global unable, able
    unable = set()
    able = set()
    for i, list_val in dic.items():
        if not i in visited:
            unable |= set(list_val)
    unable |= visited
    able =allset-unable

for tc in range(10):
    V, E = map(int,input().split())
    data = list(map(int,input().split()))
    visited = set()
    allset = set(i+1 for i in range(V))

    dic = {}
    unable = set()
    able = set()
    result = []

    for i in range(V):
        dic[i+1] = []
    
    for j in range(E):
        start = data[j*2]
        end = data[j*2+1]
        dic[start].append(end)

    while len(visited) != V:
        find()
        for k in able:
            visited.add(k)
            result.append(k)
    # print(f"#{tc+1}", end = " ")
    # print(*result)




# 2차원 배열로 간선 표시
# for tc in range(10):
#     V, E = map(int,input().split())
#     data = list(map(int,input().split()))
#     matrix = [[0]*V for _2 in range(V)]
#     visited = [0]*V
#     result = []
#
#     for i in range(E):
#         start = data[i*2]-1
#         end = data[i*2+1]-1
#         matrix[start][end] = 1
#
#     pos = [1]*V
#     while len(result) != V:
#         impos = []
#         for i in range(V):
#             for j in range(V):
#                 if matrix[i][j] and not visited[i]:
#                     impos.append(j)
#
#         for k in range(len(impos)):
#             pos[impos[k]] = 0
#
#         for u in range(len(pos)):
#             if pos[u]:
#                 visited[u] = 1
#                 result.append(u+1)
#                 pos[u] = 0
#             elif not visited[u]:
#                 pos[u] = 1
#
#     print(f"#{tc+1}", end = " ")
#     print(*result)
=======
T = 10

V, E = map(int, input().split())
temp = list(map(int,input().split()))
data = []

for i in range(E):
    data.append((temp[i], temp[i+1]))
print(temp)
print(data)

# queue = []
# result = []
# data = [[0 for _ in range(V+1)] for a in range(V+1)]
# visited = [0 for i in range(V+1)]
#
# for i in range(0, len(temp),2):
#     data[temp[i]][temp[i + 1]] = 1
#
# print(temp)
# print(data)
#
# for i in range(V+1):
#     print('{} {}'.format(i,data[i]))
#
flag = 1
for i in range(V+1):
    if data[i][i] == 0:
        flag = 0
>>>>>>> a0051c1da259acfa5e5302e9e03534c3a9fe7763
