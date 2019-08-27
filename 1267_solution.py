import sys
sys.stdin = open('1267.txt')

def make_spread(n,lines):
    spread=[[] for i in range(n+1)]
    for i in range(len(lines)//2):
        spread[lines[2*i+1]].append(lines[2*i])
    for i in range(len(spread)):
        spread[i]=list(set(spread[i]))
    return (spread)


def check_all_visited(dots):
    global visited
    for i in dots:
        if visited[i]==0:
            return i
    return 'f'


def dfs(start,target):
    global visited
    global result
    stack=[0]*(n+1)
    top=-1

    top=0
    stack[top]=start
    visited[start]=1
    current=start

    while (top!=-1):
        d=check_all_visited(target[current])
        if d!='f':
            top+=1
            stack[top]=d
            visited[d]=1
            current=d  #
        else:
            result.append(current)
            top-=1
            current=stack[top]

    return result




for t in range(1,11):
    n,k=list(map(int,input().split()))
    lines=list(map(int,input().split()))
    spread=make_spread(n,lines)
    visited=[0]*(n+1)
    result=[]
    for i in range(1,n+1):
        if visited[i]==0:
            dfs(i,spread)

    print(f"#{t} {' '.join(list(map(str,result)))}")