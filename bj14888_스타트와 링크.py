
def comb(c,idx):

    if c == int(N/2):
        teams.append(group1[:N//2])
        return

    for i in range(idx,N):
        group1[c] = member[i]
        comb(c+1,i+1)

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
member = [_ for _ in range(1,N+1)]
group1 = [0]*N
teams = []
result = 0xfffffff
comb(0,0)

for i in range(len(teams)//2):
    t1 = teams[i]
    t2 = teams[-(i+1)]
    tp1 = 0
    tp2 = 0

    for y in range(N//2):
        for x in range(N//2):
           if y != x:
               tp1 += data[t1[y]-1][t1[x]-1]
               tp2 += data[t2[y]-1][t2[x]-1]
    temp = abs(tp1-tp2)
    if result > temp:
        result = temp
print(result)

#  (1, 3, 6), (2, 4, 5)
#  2+5, 1+5, 1+3 = 7+6+4 = 17 | 3+4, 2+4, 2+4 = 20
# print('  ',end=' ')
# for i in range(N):
#     print(i+1,end='  ')
# print()
# for i in range(N):
#     print(i+1,data[i])
