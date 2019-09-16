import sys
sys.stdin = open('1493.txt')

def sharp(x,y):
    result = 0
    for i in range(1, x + 1):
        result += i
    for j in range(2, y + 1):
        result += x + (j - 2)
    return result

def amp(num):
    # global rx,ry
    rx,ry = 0,0
    nx,ny = 1,1
    temp = sharp(nx,ny)
    if temp == num:
        return nx,ny

    while temp < num:
        ny += 1
        temp = sharp(nx, ny)
        if temp ==num:
            return nx,ny


    c = ny-1
    for j in range(1,c+1):
        temp = sharp(j, c+1 - j)
        rx, ry = j, c+1 - j
        # print(temp,num)
        # print('rx,ry',rx,ry)
        if temp == num:
            # print(temp,num)
            return (rx, ry)


def myadd(a,b):
    return (a[0]+b[0]),(a[1]+b[1])

def star(p,q):
    a,b = myadd(amp(p),amp(q))
    return sharp(a,b)


T = int(input())
for tc in range(1,T+1):
    data =list(map(int,input().split()))
    print("#{} {}".format(tc,star(data[0],data[1])))