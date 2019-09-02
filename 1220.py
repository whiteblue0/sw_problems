import sys
sys.stdin = open('1220.txt')

T = 10
for tc in range(1,T+1):

    N = int(input())
    temp = []
    for _ in range(N):
        temp.append(list(map(int, input().split())))

    data = []
    for i in range(N):
        lst = []
        for j in range(len(temp[i])):
            if temp[j][i]:
                lst.append(temp[j][i])
        data.append(lst)

    cnt = 0
    for i in range(len(data)):
        for j in range(len(data[i])-1):
            if data[i][j] == 1 and data[i][j+1] == 2:
                cnt += 1

    print('#{} {}'.format(tc,cnt))




# cnt = 0
#
# stack1 = []
# stack2 = []
# for i in range(N):
#     cnt = 0
#     j = -1
#     while j < N:
#         j += 1
#         print('i:', i)
#         print('j:', j)
#         print('cnt', cnt)
#         if j == N-1:
#             break
#
#         if data[j][i] == 1:
#             for k in range(j+1,N):
#                 if data[k][i] == 1:
#                     print('{},data = 1'.format(k))
#                     j = k
#                     break
#                 elif data[k][i] == 2:
#                     cnt += 1
#                     print('{},data = 2'.format(k))
#                     j = k
#                     break