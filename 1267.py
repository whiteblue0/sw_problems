import sys
sys.stdin = open('1267.txt')

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
