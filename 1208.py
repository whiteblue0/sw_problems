import sys
sys.stdin = open('1208.txt')

T = 10

for a in range(1,T+1):
    cnt = int(input())
    box = list(map(int, input().split()))
    mymin = 100
    minidx = 0
    mymax = 0
    maxidx = 0
    while cnt > 0:
        for i in range(len(box)):
            if box[i] <= mymin:
                mymin = box[i]
                minidx = i
            if box[i] >= mymax:
                mymax = box[i]
                maxidx = i


        box[maxidx] -= 1
        box[minidx] += 1
        mymax -= 1
        mymin +=1

        for i in range(len(box)):
            if box[i] <= mymin:
                mymin = box[i]
                minidx = i
            if box[i] >= mymax:
                mymax = box[i]
                maxidx = i
        cnt -= 1


    print('#{} {}'.format(a , mymax-mymin))