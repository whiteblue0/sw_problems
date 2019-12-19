N,M = map(int,input().split())
data = [[0]*M for _ in range(M)]
for i in range(N):
    t = input()
    for j in range(len(t)):
        if t[j] == "#":
            data[i][j] = 9
        elif t[j] == ".":
            data[i][j] = 0
        elif t[j] == "B":
            data[i][j] = 2
        elif t[j] == "R":
            data[i][j] = 1
        else:
            data[i][j] = 3

for i in range(N):
    print(data[i])
