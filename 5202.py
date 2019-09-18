import sys
sys.stdin = open("5202.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort()

    line = []

    for i in range(N):
        if not line:
            line.append(data[i])
        elif line[-1][1] <= data[i][0]:
            line.append(data[i])
    result = len(line)
    print("#{} {}".format(tc,result))