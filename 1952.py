def f(n, s): 
    global myMin
    if(n >= 13):
        if(s < myMin):
            myMin = s
    else:
        f(n+1, s+d*month[n])
        f(n+1, s+m)
        f(n+3, s+m3)

T = int(input())
for tc in range(T):
    d, m, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    myMin = y
    f(1, 0)
    print("#{} {}".format(tc+1, myMin))