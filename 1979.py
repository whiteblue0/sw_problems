import sys
sys.stdin = open('1979.txt')

#
# T = int(input())
#
# for a in range(T):
#     arr = []
#     N, K = map(int, input().split())
#     for i in range(N):
#         arr.append(list(map(int, input().split())))
#
#     fit = 0
#
#     for j in range(N):
#         cnt = 0
#         for i in range(N):
#             if arr[j][i] == 1:
#                 cnt += 1
#                 if cnt == K:
#                     if i == N-1:
#                         fit += 1
#                         cnt = 0
#                     elif arr[j][i+1] == 0:
#                         fit += 1
#                         cnt = 0
#                 elif cnt > K:
#                     cnt = 0
#             else:
#                 cnt = 0
#
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if arr[j][i] == 1:
#                 cnt += 1
#                 if cnt == K:
#                     if j == N-1:
#                         fit += 1
#                         cnt = 0
#                     elif arr[j+1][i] == 0:
#                         fit += 1
#                         cnt = 0
#                 elif cnt > K:
#                     cnt = 0
#             else:
#                 cnt = 0
#
#     print('#{} {}'.format(a+1, fit))
#
<<<<<<< HEAD

=======
#
>>>>>>> 3493ec70266b67dea9a25aeb34037fbc2e499f95
def xblock(y,x):
    if x == N-1 or not puzzle[y][x+1]:
        return True
    else:
        return False
def yblock(y,x):
    if y == N-1 or not puzzle[y+1][x]:
        return True
    else:
        return False

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())

    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
<<<<<<< HEAD
=======

    cnt = 0
    for i in range(N):
        temp=0
        for j in range(N):
            if puzzle[i][j] == 1:
                temp += 1
                if temp==K:
                    if xblock(i,j):
                        cnt+=1

            else:
                temp = 0
    # print('#',tc)
    # print('x',cnt,end=' ')
    # cnt = 0
>>>>>>> 3493ec70266b67dea9a25aeb34037fbc2e499f95

    cnt = 0
    for i in range(N):
        temp=0
        for j in range(N):
<<<<<<< HEAD
            if puzzle[i][j] == 1:
                temp += 1
                if temp==K:
                    if xblock(i,j):
=======
            if puzzle[j][i] == 1:
                temp += 1
                if temp==K:
                    if yblock(j,i):
>>>>>>> 3493ec70266b67dea9a25aeb34037fbc2e499f95
                        cnt+=1

            else:
                temp = 0
<<<<<<< HEAD
    # print('#',tc)
    # print('x',cnt,end=' ')
    # cnt = 0

    for i in range(N):
        temp=0
        for j in range(N):
            if puzzle[j][i] == 1:
                temp += 1
                if temp==K:
                    if yblock(j,i):
                        cnt+=1

            else:
                temp = 0
    # print('y',cnt)
=======
    # print('y',cnt)

    print('#{} {}'.format(tc, cnt))
>>>>>>> 3493ec70266b67dea9a25aeb34037fbc2e499f95

    print('#{} {}'.format(tc, cnt))