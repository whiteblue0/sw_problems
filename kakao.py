# 문제1.
# board = [[0,0,0,0,0],
#          [0,0,1,0,3],
#          [0,2,5,0,1],
#          [4,2,4,4,2],
#          [3,5,1,3,1]]
# N = len(board)
# moves = [1,5,3,5,1,2,1,4]
# stack = []
# result = 0
# for i in range(len(moves)):
#     target = moves.pop(0)-1
#     j = 0
#     crain = 0
#     while j < N:
#         if board[j][target]:
#             crain = board[j][target]
#             if stack and stack[-1] == crain:
#                 stack.pop()
#                 result += 2
#             else:
#                 stack.append(crain)
#             board[j][target] = 0
#             break
#         j += 1

# 문제2.
# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# s = s.strip('{}')
# s = s.split('},{')
# for i in range(len(s)):
#      s[i] = s[i].split(',')
#      for j in range(len(s[i])):
#          s[i][j] = int(s[i][j])
# lst = [0]*len(s)
# for numset in s:
#     lst[len(numset)-1] = numset
# tup = []
# for i in range(len(lst)):
#     for num in lst[i]:
#         if not num in tup:
#             tup.append(num)
# answer = tup

# 문제3.
def dfs(n):

    pass

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
checklist = [list()]*len(banned_id)
for i in range(len(banned_id)):
    for j in range(len(user_id)):
        if len(user_id[j]) == len(banned_id[i]):
            flag = 1
            for k in range(len(banned_id[i])):
                if banned_id[i][k] != user_id[j][k] and banned_id[i][k] != "*":
                    flag = 0
                    break
            if flag and not user_id[j] in checklist[i]:
                checklist[i].append(user_id[j])
print(checklist)



# 문제4.
# k = 10
# room_number = [1,3,4,1,3,1]
# room = [0]*k
# result = []
# for i in range(len(room_number)):
#     if not room[room_number[i]]:
#         room[room_number[i]] = 1
#         result.append(room_number[i])
#     else:
#         cnt = 1
#         while True:
#             if room[room_number[i]+cnt]:
#                 cnt += 1
#             else:
#                 room[room_number[i]+cnt] = 1
#                 result.append(room_number[i]+cnt)
#                 break
# print(result)

