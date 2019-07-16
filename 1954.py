# import sys
# sys.stdin = open('input.txt')

T = int(input())

size = int(input())
cnt = 1
turn = 0

Matrix = [[0]*size for i in range(size)]
y= 0

for x in range(size-turn):
    Matrix[y][x]=cnt
    print(Matrix)
    cnt+=1

while cnt < (size**2):
    for y in range(turn+1,size-turn):
        Matrix[y][x]=cnt
        print(Matrix)
        cnt+=1

    for x in range(size-(turn+2),(turn-1),-1):
        Matrix[y][x]=cnt
        print(Matrix)
        cnt+=1
        turn+=1

    for y in range(size-(turn+1), (turn-1), -1):
        Matrix[y][x]=cnt
        print(Matrix)
        cnt+=1

    for x in range(turn+1,size-turn):
        Matrix[y][x] = cnt
        print(Matrix)
        cnt+=1
        turn+=1

print(Matrix)