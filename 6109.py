import sys
sys.stdin = open('6109.txt')

T = int(input())
for tc in range(1,T+1):
    N,D = input().split()
    N = int(N)
    data = [list(map(int,input().split())) for _ in range(N)]

    if D == 'up':
        for i in range(N):
            for j in range(N-1):
                if data[j][i] == 0:
                    for k in range(j+1,N):
                        if data[k][i]:
                            data[j][i], data[k][i] = data[k][i], data[j][i]
                            break
        for i in range(N):
            for j in range(N-1):
                if data[j][i] ==data[j+1][i]:
                    data[j][i] *= 2
                    data[j+1][i] = 0

        for i in range(N):
            for j in range(N-1):
                if data[j][i] == 0:
                    for k in range(j+1,N):
                        if data[k][i]:
                            data[j][i], data[k][i] = data[k][i], data[j][i]
                            break

    elif D == 'down':
        for i in range(N-1,-1,-1):
            for j in range(N-1,0,-1):
                if data[j][i] == 0:
                    for k in range(j-1,-1,-1):
                        if data[k][i]:
                            data[j][i], data[k][i] = data[k][i], data[j][i]
                            break
        for i in range(N-1,-1,-1):
            for j in range(N-1,0,-1):
                if data[j][i] ==data[j-1][i]:
                    data[j][i] *= 2
                    data[j-1][i] = 0

        for i in range(N-1,-1,-1):
            for j in range(N-1,0,-1):
                if data[j][i] == 0:
                    for k in range(j-1,-1,-1):
                        if data[k][i]:
                            data[j][i], data[k][i] = data[k][i], data[j][i]
                            break

    elif D == 'left':
        for i in range(N):
            for j in range(N-1):
                if data[i][j] == 0:
                    for k in range(j+1,N):
                        if data[i][k]:
                            data[i][j], data[i][k] = data[i][k], data[i][j]
                            break

        for i in range(N):
            for j in range(N-1):
                if data[i][j] ==data[i][j+1]:
                    data[i][j] *= 2
                    data[i][j+1] = 0

        for i in range(N):
            for j in range(N-1):
                if data[i][j] == 0:
                    for k in range(j+1,N):
                        if data[i][k]:
                            data[i][j], data[i][k] = data[i][k], data[i][j]
                            break

    elif D == 'right':
        for i in range(N-1,-1,-1):
            for j in range(N-1,0,-1):
                if data[i][j] == 0:
                    for k in range(j-1,-1,-1):
                        if data[i][k]:
                            data[i][j], data[i][k] = data[i][k], data[i][j]
                            break

        for i in range(N-1,-1,-1):
            for j in range(N-1,0,-1):
                if data[i][j] ==data[i][j-1]:
                    data[i][j] *= 2
                    data[i][j-1] = 0

        for i in range(N-1,-1,-1):
            for j in range(N-1,0,-1):
                if data[i][j] == 0:
                    for k in range(j-1,-1,-1):
                        if data[i][k]:
                            data[i][j], data[i][k] = data[i][k], data[i][j]
                            break

    print("#{}".format(tc),end='')
    for i in range(N):
        print()
        for j in range(len(data[i])):
            print(data[i][j],end=' ')
    print()