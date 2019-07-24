import sys
sys.stdin = open('input.txt')

T = int(input())

for q in range(T):
    cnt = 1
    arr = []
    for i in range(9):
        arr.append(list(map(int, input().split())))
    while cnt == 1 :
        for x in range(9):
            if sum(arr[x]) != 45:
                cnt = 0

            ysum=0
            for y in range(9):
                ysum = arr[y][x]
                print(ysum)
            if ysum != 45:
                cnt = 0

        for b in range(3):
            for a in range(3):
                sqr = 0
                for j in range(3):
                    for i in range(3):
                       sqr += arr[j + 3*b][i + 3*a]
                if sqr != 45:
                    cnt = 0
        break
    print('#{} {}'.format(q + 1, cnt))