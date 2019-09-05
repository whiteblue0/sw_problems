import sys
sys.stdin = open('1486.txt')

def subset(c,k,mysum):
    global mymin
    result = counter[:c]
    if mymin < mysum:
        return

    if c==N:
        if mysum>=B:
            if mymin>mysum:
                mymin=mysum
            return

    else:
        subset(c+1,k+1,mysum+data[k])
        subset(c+1,k+1,mysum)

T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    data = list(map(int, input().split()))
    counter = [0]*N
    mymin = 987654321
    subset(0,0,0)

    print("#{} {}".format(tc,(mymin-B)))