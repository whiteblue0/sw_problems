T = input()
P = input()
LT = len(T)
LP = len(P)
que = 0
ans = []

while que < (LT-LP):
    cnt = 0
    for j in LP:
        if LP[j] != LT[que+j]:
            que += j
            break
        cnt += 1
    if cnt == LP:
        ans.append(que)
