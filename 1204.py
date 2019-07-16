import sys
sys.stdin = open('input.txt')

Case = int(input())

for i in range(1,Case+1):
    testnum = int(input())
    testcase = list(map(int,input().split()))

    cnt = 0
    output = []  # index = 점수, value = 빈도수
    for i in range(100, -1,-1):
        cnt = testcase.count(100-i)
        output.append(cnt)
    m = max(output)
    k = [x for x, y in enumerate(output) if y ==m ]
    print('#{} {}'.format(testnum, max(k)))

