import sys
sys.stdin = open('가장 긴 수열.txt')

T = int(input())




for tc in range(1,T+1):
    N=list(map(int,input().split()))
    cnt=0

    for i in range(len(N)):
        temp=[]
        temp.append(N[i])
        for j in range(i,len(N)):
            if temp[-1] > N[j]:
                temp.append(N[j])
        for k in range(i,0,-1):
            if temp[0] > N[k]:
                temp.insert(0,N[k])


        if cnt <= len(temp):
            cnt=len(temp)
        print(temp)
    print('#{} {}'.format(tc,cnt))