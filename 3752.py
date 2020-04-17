T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
    ans = set([0])
    for i in range(len(data)):
        scoreset = set()
        for j in ans:
            scoreset.add(data[i]+j)
        ans = set(list(ans)+list(scoreset))
    print("#{} {}".format(tc,len(ans)))