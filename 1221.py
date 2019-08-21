import sys
sys.stdin = open('1221.txt')

table = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for tc in range(T):
    N = input()
    case = input().split()
    cnt = [0*n for n in range(10)]

    for i in case:
        for j in range(len(table)):
            if i == table[j]:
                cnt[j] += 1

    print('#{}'.format(tc+1))
    for i in range(len(cnt)):
        print((table[i]+" ")*cnt[i],end='')
    print()



# for tc in range(T):
#     N = input()
#     case = input().split()
#     trans = []
#
#     lc = len(case)
#     lt = len(table)
#
#     for i in range(lc):
#         for j in range(lt):
#             if case[i] == table[j]:
#                 trans.append(j)
#
#     for i in range(len(trans)-1, 0, -1):
#         for j in range(0, i):
#             if trans[j] > trans[j+1]:
#                 trans[j], trans[j+1] = trans[j+1], trans[j]
#
#     print('#{} '.format(tc+1))
#     for i in range(len(trans)):
#         if i == len(trans)-1:
#             print(table[trans[i]])
#         else:
#             print(table[trans[i]],end=' ')