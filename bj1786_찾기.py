T = input()
P = input()
LT = len(T)
LP = len(P)
que = 0
ans = []
pattern = []
temp = 0
for i in range(LP):
    if P[i] == P[0]:
        for j in range(LP-i):
            if P[i+j] != P[j]:
                break
            else:
                pattern.append(P[i+j])


while que <= (LT-LP):
    cnt = 0
    for i in range(LP):
        if P[i] == T[que+i]:
            pattern.append(P[i])
        else:

        cnt += 1
    if cnt == LP:
        ans.append(que)
        que += 1

print(len(ans))
for i in range(len(ans)):
    if i == len(ans):
        print(ans[i])
    else:
        print(ans[i],end='')