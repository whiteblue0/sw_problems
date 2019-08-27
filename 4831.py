import sys
sys.stdin = open('4831.txt')

T = int(input())

for a in range(1,T+1):
    K, N, M = map(int, input().split())  # 한번에 갈수있는 거리, 종점거리,충전기 개수
    Crg = list(map(int, input().split()))  # 충전기 위치
    able=0
    cnt = 0

    while able < N:
        if able+K >= N:
           break
        elif able+K in Crg:
            cnt += 1
            able += K
        else:
            pos2 = able
            for i in range(able+K,able,-1):
                if i in Crg:
                    cnt += 1
                    pos2 = i
                    break
            if pos2 == able:
                cnt = 0
                break
            else:
                able = pos2

    print('#{} {}'.format(a, cnt))