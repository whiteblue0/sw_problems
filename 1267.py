import sys
sys.stdin = open('1267.txt')

def find():
    global unable, able
    unable = set()
    able = set()
    for i, list_val in dic.items():
        if not i in visited:
            unable |= set(list_val)
    unable |= visited   # | : 합집합
    able =allset-unable

for tc in range(10):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
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

    print(dic)

    while len(visited) != V:
        find()
        for k in able:
            visited.add(k)
            result.append(k)
    # print("#{}".format(tc+1), end = " ")
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

