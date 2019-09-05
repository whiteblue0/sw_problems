import sys
sys.stdin = open('5209.txt')


def dfs(y,cnt):
    global myMin
    # 종료조건
    if y==N:
        # 최소값, 최대값, 끝날때 로직
        if myMin>cnt:
            myMin=cnt
        return
    # 가지치기 조건

    # 현재 상태(Y)에서 찾을수 있는 모든 경우
    for x in range(N):
        # 누적된 상태에서 걸리는 조건들
        if not visited[x]:
            # 상태를 누적
            visited[x]=1

            # 다음 단계 진입
            dfs(y+1,cnt+data[y][x])

            # 상태 초기화
            visited[x]=0


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    data=[list(map(int,input().split())) for _ in range(N)]
    visited=[0]*N
    myMin=987654321
    dfs(0,0)

    print('#{} {}'.format(tc,myMin))