import sys
sys.stdin = open('4831.txt')

T = int(input())

for a in range(1,T+1):
    K, N, M = map(int, input().split())  # 한번에 갈수있는 거리, 종점거리,충전기 개수
    Crg = list(map(int, input().split()))  # 충전기 위치
    pos=0
    cnt = 0

    while pos < N:
        if pos+K >= N:
           break
        elif pos+K in Crg:
            cnt += 1
            pos += K
        else:
            pos2 = pos
            for i in range(pos+K, pos, -1):
                if i in Crg:
                    cnt += 1
                    pos2 = i
                    break
            if pos2 == pos:
                cnt = 0
                break
            else:
                pos = pos2

    print('#{} {}'.format(a, cnt))