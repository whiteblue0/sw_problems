import sys
sys.stdin = open("5201.txt")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    container = list(map(int, input().split()))
    container.sort(reverse=True)
    truck = list(map(int, input().split()))
    truck.sort(reverse=True)

    departed = [0]*M
    empty = [0]*N

    for i in range(M):
        for j in range(N):
            if truck[i]>=container[j] and departed[i] == 0 and empty[j] == 0:
                departed[i] = container[j]
                empty[j] = 1
                continue
    print("#{} {}".format(tc,sum(departed)))